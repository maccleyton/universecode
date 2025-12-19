
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('collapsed');
}

/* =========================================================
   TOC ACTIVE + IntersectionObserver robusto
   - Funciona com href="#id" e href="./cap01.html#id"
   - Observa somente os IDs que o TOC aponta (bem mais estável)
   - Usa o container de rolagem (.book-content-wrapper) como root
========================================================= */

/* ---------- Helpers de URL / Hash ---------- */
function normalizeFileName(pathname) {
  if (!pathname) return "";
  const parts = pathname.split("/");
  return parts[parts.length - 1] || "";
}

function getHrefHash(href) {
  if (!href) return "";
  const idx = href.indexOf("#");
  return idx === -1 ? "" : href.slice(idx); // inclui '#'
}

function getHrefId(href) {
  const hash = getHrefHash(href);
  if (!hash) return "";
  return hash.startsWith("#") ? hash.slice(1) : hash;
}

function resolveHref(href) {
  try { return new URL(href, window.location.href); }
  catch { return null; }
}

function isSameDocumentLink(href) {
  // true se o link aponta para o arquivo atual (ou é só "#id")
  if (!href) return false;

  // caso "#id"
  if (href.startsWith("#")) return true;

  const u = resolveHref(href);
  if (!u) return false;

  const curFile = normalizeFileName(window.location.pathname);
  const linkFile = normalizeFileName(u.pathname);

  return curFile === linkFile;
}

/* ---------- Achar o melhor link do TOC para um id ---------- */
function findBestTocItemById(id) {
  if (!id) return null;

  const targetHash = "#" + id;
  const currentFile = normalizeFileName(window.location.pathname);

  const tocItems = document.querySelectorAll(".toc-item[href]");

  // 1) prioridade: mesmo arquivo + mesmo hash
  for (const a of tocItems) {
    const href = a.getAttribute("href") || "";
    const url = resolveHref(href);

    if (url) {
      const file = normalizeFileName(url.pathname);
      const hash = url.hash || "";
      if (file === currentFile && hash === targetHash) return a;
    } else {
      // fallback: se não conseguir resolver, tenta pelo hash do href
      const hash = getHrefHash(href);
      if (hash === targetHash) return a;
    }
  }

  // 2) fallback: qualquer href que tenha o mesmo hash (#id)
  for (const a of tocItems) {
    const href = a.getAttribute("href") || "";
    const hash = getHrefHash(href);
    if (hash === targetHash) return a;
  }

  return null;
}

function setActiveTocById(id) {
  const items = document.querySelectorAll(".toc-item");
  items.forEach(i => i.classList.remove("active"));

  const active = findBestTocItemById(id);
  if (active) {
    active.classList.add("active");
    active.scrollIntoView({ block: "nearest" });
  }
}

function getHashIdFromLocation() {
  const h = window.location.hash || "";
  if (!h) return "";
  try { return decodeURIComponent(h.slice(1)); }
  catch { return h.slice(1); }
}

/* ---------- Scroll correto dentro do wrapper ---------- */
const scroller = document.querySelector(".book-content-wrapper") || null;

function scrollToIdInsideWrapper(id, behavior) {
  if (!id) return;
  const el = document.getElementById(id);
  if (!el) return;

  // se não existir wrapper, cai no comportamento padrão
  const opts = { behavior: behavior || "smooth", block: "start" };
  el.scrollIntoView(opts);
}

/* ---------- Observer (com root correto) ---------- */
// Em capítulos longos, usar threshold 0 é MUITO mais estável.
// rootMargin define uma “linha de ativação” (topo da tela, com folga).
const observerOptions = {
  root: scroller,                 // importante: observar dentro do container rolável
  rootMargin: "-20% 0px -70% 0px", // ajuste fino (pode calibrar depois)
  threshold: 0
};

const observer = new IntersectionObserver((entries) => {
  // Se vários entram ao mesmo tempo, escolhemos o que está mais próximo do topo
  let best = null;

  for (const entry of entries) {
    if (!entry.isIntersecting) continue;

    const id = entry.target.getAttribute("id");
    if (!id) continue;

    if (!best) {
      best = entry;
    } else {
      const bestTop = best.boundingClientRect.top;
      const curTop  = entry.boundingClientRect.top;
      if (curTop < bestTop) best = entry;
    }
  }

  if (best) {
    const id = best.target.getAttribute("id");
    if (id) setActiveTocById(id);
  }
}, observerOptions);

/* ---------- Observar apenas IDs apontados pelo TOC ---------- */
function observeTargetsFromToc() {
  const tocItems = document.querySelectorAll(".toc-item[href]");
  const seen = new Set();

  for (const a of tocItems) {
    const href = a.getAttribute("href") || "";
    const id = getHrefId(href);
    if (!id) continue;

    // Só observa se o alvo existir NESTA página
    // (isso resolve o cap01, que tem links "#prologo" mas o id não existe nele)
    const target = document.getElementById(id);
    if (!target) continue;

    // Evita observar repetido
    if (seen.has(id)) continue;
    seen.add(id);

    observer.observe(target);
  }
}

/* ---------- Sincronização inicial (quando entra por link+id) ---------- */
function syncFromHashOnLoad() {
  const id = getHashIdFromLocation();
  if (!id) return;

  // 1) marca ativo
  setActiveTocById(id);

  // 2) faz scroll dentro do wrapper (garante funcionar mesmo no file://)
  // Pequeno delay ajuda quando a página ainda está “assentando” layout
  setTimeout(() => scrollToIdInsideWrapper(id, "auto"), 30);
}

/* ---------- Clique no TOC ---------- */
function bindTocClicks() {
  document.addEventListener("click", (e) => {
    const a = e.target.closest(".toc-item");
    if (!a) return;

    const href = a.getAttribute("href") || "";
    const id = getHrefId(href);

    // Se for link para esta mesma página, fazemos navegação “controlada”
    // (para scroll suave no wrapper + highlight imediato)
    if (id && isSameDocumentLink(href)) {
      e.preventDefault();

      // atualiza URL sem recarregar
      if (window.location.hash !== ("#" + id)) {
        history.pushState(null, "", "#" + id);
      }

      setActiveTocById(id);
      scrollToIdInsideWrapper(id, "smooth");
      return;
    }

    // Se for link para outra página, deixa o navegador navegar normalmente.
    // (o highlight vai acontecer na outra página via syncFromHashOnLoad)
  });
}

/* ---------- Init geral ---------- */
function initTocSync() {
  observeTargetsFromToc();
  bindTocClicks();
  syncFromHashOnLoad();

  // Quando muda hash na mesma página (ex.: back/forward do navegador)
  window.addEventListener("hashchange", () => {
    const id = getHashIdFromLocation();
    if (!id) return;
    setActiveTocById(id);
    scrollToIdInsideWrapper(id, "smooth");
  });
}

/* ---------- Start ---------- */
// DOM pronto já é suficiente para observar e bindar
document.addEventListener("DOMContentLoaded", initTocSync);

// Para garantir em casos pesados (capítulos enormes), reforça também no load
window.addEventListener("load", () => {
  // Se DOMContentLoaded já rodou, isso só reforça a sync inicial
  syncFromHashOnLoad();
});
