
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('collapsed');
}

/* =========================================================
   UNIFIED TOC GENERATION
   - Dynamically populates .sidebar-content
   - Links to all chapters
   - Generates local sections for current page
========================================================= */

const bookTOC = [
  { title: "Prólogo: O Grande Teatro Da Realidade", file: "prologo.html" },
  { title: "Apresentação: Um Convite à Jornada Cósmica", file: "apresentacao.html" },
  { type: "part", title: "Parte I: Os Fundamentos do Universo", file: "parte01.html" },
  { title: "Capítulo 01: As Bases da Realidade", file: "capitulo_01.html" },
  { type: "part", title: "Parte II: O Nascimento do Tempo e Espaço", file: "parte02.html" },
  { title: "Capítulo 02: O Big Bang e a Era de Planck", file: "capitulo_02.html" },
  { title: "Capítulo 03: Era da Grande Unificação", file: "capitulo_03.html" },
  { title: "Capítulo 04: Era Eletrofraca", file: "capitulo_04.html" },
  { title: "Capítulo 05: Era Hadrônica", file: "capitulo_05.html" },
  { title: "Capítulo 06: Era dos Léptons", file: "capitulo_06.html" },
  { title: "Capítulo 07: Nucleossíntese Primordial", file: "capitulo_07.html" },
  { title: "Capítulo 08: Era da Radiação", file: "capitulo_08.html" },
  { type: "part", title: "Parte III: A Emergência da Complexidade", file: "parte03.html" },
  { title: "Capítulo 09: Recombinação e Desacoplamento", file: "capitulo_09.html" },
  { title: "Capítulo 10: Idade das Trevas", file: "capitulo_10.html" },
  { title: "Capítulo 11: Primeiras Estrelas (Pop. III)", file: "capitulo_11.html" },
  { title: "Capítulo 12: Primeiras Supernovas", file: "capitulo_12.html" },
  { type: "part", title: "Parte IV: A Complexificação Química", file: "parte04.html" },
  { title: "Capítulo 13: Segunda Geração Estelar", file: "capitulo_13.html" },
  { title: "Capítulo 14: Primeiras Galáxias e Quasares", file: "capitulo_14.html" },
  { title: "Capítulo 15: Evolução Química Cósmica", file: "capitulo_15.html" },
  { type: "part", title: "Parte V: Nascimento do Sistema Solar", file: "parte05.html" },
  { title: "Capítulo 16: Formação do Sistema Solar", file: "capitulo_16.html" },
  { title: "Capítulo 17: Terra Primitiva (Hadeano)", file: "capitulo_17.html" },
  { type: "part", title: "Parte VI: Origem e Evolução da Vida", file: "parte06.html" },
  { title: "Capítulo 18: Origem da Vida (Arqueano)", file: "capitulo_18.html" },
  { title: "Capítulo 19: Primeiros Organismos", file: "capitulo_19.html" },
  { title: "Capítulo 20: Revolução do Oxigênio", file: "capitulo_20.html" },
  { title: "Capítulo 21: Células Eucarióticas", file: "capitulo_21.html" },
  { title: "Capítulo 22: Evolução Multicelular", file: "capitulo_22.html" },
  { type: "part", title: "Parte VII: Explosão da Complexidade Biológica", file: "parte07.html" },
  { title: "Capítulo 23: Explosão Cambriana", file: "capitulo_23.html" },
  { title: "Capítulo 24: Conquista da Terra", file: "capitulo_24.html" },
  { title: "Capítulo 25: Florestas e Ecossistemas", file: "capitulo_25.html" },
  { title: "Capítulo 26: Extinções em Massa", file: "capitulo_26.html" },
  { title: "Capítulo 27: Era dos Dinossauros", file: "capitulo_27.html" },
  { title: "Capítulo 28: Evolução dos Mamíferos", file: "capitulo_28.html" },
  { type: "part", title: "Parte VIII: Evolução da Inteligência e Consciência", file: "parte08.html" },
  { title: "Capítulo 29: Evolução do Cérebro", file: "capitulo_29.html" },
  { title: "Capítulo 30: Evolução Humana", file: "capitulo_30.html" },
  { title: "Capítulo 31: Tecnologia e Civilização", file: "capitulo_31.html" },
  { type: "part", title: "Parte IX: O Presente Cósmico e Biológico", file: "parte09.html" },
  { title: "Capítulo 32: Terra no Antropoceno", file: "capitulo_32.html" },
  { title: "Capítulo 33: Fronteiras da Ciência Atual", file: "capitulo_33.html" },
  { type: "part", title: "Parte X: Futuro da Vida e do Universo", file: "parte10.html" },
  { title: "Capítulo 34: Evolução Futura da Vida", file: "capitulo_34.html" },
  { title: "Capítulo 35: Destino do Sistema Solar", file: "capitulo_35.html" },
  { title: "Capítulo 36: Era Estelar do Universo", file: "capitulo_36.html" },
  { title: "Capítulo 37: Era Degenerada", file: "capitulo_37.html" },
  { title: "Capítulo 38: Era dos Buracos Negros", file: "capitulo_38.html" },
  { title: "Capítulo 39: Era das Partículas", file: "capitulo_39.html" },
  { type: "part", title: "Parte XI: Síntese e Reflexões", file: "parte11.html" },
  { title: "Capítulo 40: Padrões Universais de Evolução", file: "capitulo_40.html" },
  { title: "Capítulo 41: Conectando as Escalas", file: "capitulo_41.html" },
  { title: "Capítulo 42: Questões Profundas", file: "capitulo_42.html" },
  { title: "Capítulo 43: Conclusão", file: "capitulo_43.html" },
  { title: "Encerramento: A Última Palavra", file: "encerramento.html" }
];

function renderUnifiedSidebar() {
  const nav = document.querySelector('.sidebar-content');
  if (!nav) return;

  // Clear existing static content
  nav.innerHTML = '';

  // Add Home Link
  const homeLink = document.createElement('a');
  homeLink.href = '../../index.html';
  homeLink.className = 'toc-item';
  homeLink.style.opacity = '0.7';
  homeLink.textContent = '← Voltar ao Menu';
  nav.appendChild(homeLink);

  const currentFile = normalizeFileName(window.location.pathname);

  bookTOC.forEach(item => {
    const link = document.createElement('a');

    if (item.type === 'part') {
      // Special formatting for Parts
      // Split "Parte X: Title" -> "PARTE X:<br>TITLE"
      link.className = 'toc-item';
      link.style.marginTop = '15px';
      link.style.marginBottom = '5px';
      // Optional: visual distinction
      // link.style.borderLeft = '2px solid var(--accent-color)'; // Maybe too much?

      const partsParts = item.title.split(': ');
      if (partsParts.length > 1) {
        // Uppercase both parts for consistency with user request
        const p1 = partsParts[0].toUpperCase();
        const p2 = partsParts[1].toUpperCase();
        link.innerHTML = `<span style="font-size:0.85em; opacity:0.8;">${p1}:</span><br><span style="font-weight:600;">${p2}</span>`;
      } else {
        link.textContent = item.title.toUpperCase();
      }

      if (item.file) {
        link.href = item.file;
      }
      nav.appendChild(link);

      // If this is the current file (Part Page), highlight it
      if (currentFile === item.file) {
        link.classList.add('active'); // highlight part itself
        link.classList.add('toc-sublink');
      }
      return;
    }

    // Regular Chapters / Items
    link.href = item.file;
    link.className = 'toc-item';

    const parts = item.title.split(': ');
    if (parts.length > 1) {
      link.innerHTML = `${parts[0]}:<br>${parts[1]}`;
    } else {
      link.textContent = item.title;
    }

    nav.appendChild(link);

    // If this is the active chapter, inject local sections
    if (currentFile === item.file) {
      link.classList.add('toc-sublink'); // Style as main link of current
      link.href = "#" + (document.querySelector('.book-article')?.id || ''); // Link to top of article

      // Generate local sections
      const sections = document.querySelectorAll('h3.chapter-section');

      sections.forEach(section => {
        const subLink = document.createElement('a');
        subLink.href = "#" + section.id;
        subLink.className = 'toc-item toc-sectionlink';
        subLink.innerHTML = "• " + section.innerText; // Bullet for hierarchy
        nav.appendChild(subLink);
      });

      // Add final reflections if any (usually h3 with id -sf)
      const finalRef = document.getElementById(document.querySelector('.book-article')?.id + '-sf');
      if (finalRef && !Array.from(sections).includes(finalRef)) { // if not already caught
        const subLink = document.createElement('a');
        subLink.href = "#" + finalRef.id;
        subLink.className = 'toc-item toc-sectionlink';
        subLink.innerText = "Reflexões Finais";
        nav.appendChild(subLink);
      }
    }
  });
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
      const curTop = entry.boundingClientRect.top;
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
  renderUnifiedSidebar(); // Generate the TOC first!
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
