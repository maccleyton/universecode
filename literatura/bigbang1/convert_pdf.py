
import fitz  # PyMuPDF
import os
import re

# Configurações de Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "bigbang.pdf")
OUTPUT_DIR = os.path.join(BASE_DIR, "html_output") 
ASSETS_DIR = "../assets" 

# --- CSS STYLES (Hybrid Potencial + Jornada Theme) ---
CSS_STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap');

    :root {
        /* Cores Base - Cosmos/Infinity Theme */
        --bg-app: #000000;
        --bg-panel: rgba(15, 15, 15, 0.95);
        --bg-content: #0a0a0a;
        --bg-card: #111111;

        /* Bordas */
        --border-subtle: 1px solid rgba(255, 255, 255, 0.08);
        --border-active: 1px solid rgba(255, 255, 255, 0.2);
        
        /* Texto */
        --text-primary: #ededed;
        --text-secondary: #999999;
        --text-muted: #555555;

        /* Accents */
        --accent-blue: #2997ff;
        --accent-purple: #9d4edd;
        --accent-hover: rgba(41, 151, 255, 0.15);
        --accent-color: #2997ff; /* Match user variable */

        /* Dimensões */
        --sidebar-w: 280px;
        --toolbar-h: 50px;

        /* Fonts */
        --font-ui: 'Inter', sans-serif;
        --font-body: 'Merriweather', serif;
        --font-display: 'Cinzel', serif; /* Special for Big Bang headers */
    }

    /* =========================================
       ESTILIZAÇÃO DAS SCROLLBARS (Rolagem)
       ========================================= */
    
    /* 1. Scrollbar Geral (Corpo da Página e Conteúdo) */
    ::-webkit-scrollbar {
        width: 10px;               /* Largura da barra vertical */
        height: 10px;              /* Altura da barra horizontal */
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-app); /* Fundo do trilho (Preto/Cinza Escuro) */
        border-left: 1px solid var(--border-subtle);
    }

    ::-webkit-scrollbar-thumb {
        background-color: #333;    /* Cor da barra (Cinza) */
        border-radius: 5px;        /* Bordas arredondadas */
        border: 2px solid var(--bg-app); /* Espaço entre a barra e o trilho */
    }

    ::-webkit-scrollbar-thumb:hover {
        background-color: var(--accent-color); /* Fica AZUL ao passar o mouse */
    }

    /* 2. Scrollbar Específica do TOC (Sidebar) */
    /* Garante que a barra apareça se o conteúdo for longo */
    .book-sidebar {
        overflow-y: auto;          /* Força a rolagem vertical se necessário */
        scrollbar-width: thin;     /* Firefox: barra fina */
        scrollbar-color: #333 var(--bg-card); /* Firefox: Cores */
    }

    /* Estilo Webkit (Chrome, Edge, Safari) para a Sidebar */
    .book-sidebar::-webkit-scrollbar {
        width: 6px;                /* Barra mais fina para o menu */
    }

    .book-sidebar::-webkit-scrollbar-track {
        background: var(--bg-card); /* Fundo igual ao card da sidebar */
    }

    .book-sidebar::-webkit-scrollbar-thumb {
        background-color: #444;    /* Um pouco mais claro que o fundo */
        border-radius: 3px;
        border: none;              /* Sem borda para ficar clean */
    }

    .book-sidebar::-webkit-scrollbar-thumb:hover {
        background-color: var(--accent-color); /* Azul no hover */
    }

    * { box-sizing: border-box; margin: 0; padding: 0; outline: none; }
    
    body {
        background-color: var(--bg-app);
        color: var(--text-primary);
        font-family: var(--font-ui);
        height: 100vh;
        width: 100vw;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    /* Layout Containers */
    .book-container {
        display: flex;
        flex: 1;
        overflow: hidden;
        height: 100vh;
        width: 100vw;
    }

    /* Sidebar */
    .book-sidebar {
        width: var(--sidebar-w);
        background: var(--bg-card);
        border-right: var(--border-subtle);
        display: flex;
        flex-direction: column;
        transition: margin-left 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        z-index: 10;
        flex-shrink: 0;
    }
    
    .book-sidebar.collapsed {
        margin-left: calc(var(--sidebar-w) * -1);
    }

    .sidebar-header {
        height: var(--toolbar-h);
        padding: 0 20px;
        border-bottom: var(--border-subtle);
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(22, 22, 22, 0.5);
    }

    .sidebar-title {
        font-size: 13px;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .sidebar-content {
        flex: 1;
        overflow-y: auto;
        padding: 10px 0;
    }
    
    .sidebar-content::-webkit-scrollbar { width: 4px; }
    .sidebar-content::-webkit-scrollbar-thumb { background: #333; border-radius: 2px; }

    /* TOC Items */
    .toc-item {
        display: block;
        width: 100%;
        text-align: left;
        padding: 10px 20px;
        font-size: 13px;
        color: var(--text-secondary);
        text-decoration: none;
        border-left: 3px solid transparent;
        transition: all 0.2s;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .toc-item:hover {
        background: rgba(255, 255, 255, 0.05);
        color: var(--text-primary);
    }

    .toc-item.active {
        background: var(--accent-hover);
        color: var(--accent-blue);
        border-left-color: var(--accent-blue);
        font-weight: 600;
    }
    
    .toc-group-title {
        padding: 15px 20px 5px;
        font-size: 11px;
        text-transform: uppercase;
        color: #444;
        font-weight: 700;
        letter-spacing: 1px;
        margin-top: 10px;
    }
    
    .toc-sublink {
        padding-left: 35px;
        font-size: 12px;
        color: var(--text-muted);
    }

    /* Main Area */
    .book-main {
        flex: 1;
        display: flex;
        flex-direction: column;
        background: var(--bg-app);
        position: relative;
        min-width: 0; 
    }

    /* Toolbar */
    .reader-toolbar {
        height: var(--toolbar-h);
        background: var(--bg-card);
        border-bottom: var(--border-subtle);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        flex-shrink: 0;
    }
    
    .toolbar-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--text-primary);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 60%;
    }

    .toolbar-btn {
        background: transparent;
        border: none;
        color: var(--text-secondary);
        cursor: pointer;
        padding: 6px;
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    
    .toolbar-btn:hover { background: rgba(255,255,255,0.1); color: #fff; }
    .toolbar-btn svg { width: 20px; height: 20px; stroke-width: 2; }

    /* Content Area */
    .book-content-wrapper {
        flex: 1;
        overflow-y: auto;
        padding: 40px;
        scroll-behavior: smooth;
        background: radial-gradient(circle at 50% 20%, #1a1a1a 0%, #000000 80%);
    }

    .book-article {
        max-width: 800px;
        margin: 0 auto;
        padding-bottom: 100px;
        border-bottom: 1px dashed rgba(255,255,255,0.05);
        margin-bottom: 100px;
        color: var(--text-primary);
    }

    /* TYPOGRAPHY */
    
    /* H4: Label (Parte X, Capítulo Y) */
    .book-article h4.structure-label {
        font-family: var(--font-ui);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--accent-purple);
        margin-top: 60px;
        margin-bottom: 10px;
        border-bottom: none;
    }

    /* H1: Part Title / Chapter Title Main */
    .book-article h1, .chapter-title {
        font-family: var(--font-display);
        font-size: 38px;
        font-weight: 800;
        color: #fff;
        text-align: center;
        margin-bottom: 20px;
        line-height: 1.1;
        border-bottom: 1px solid var(--border-subtle);
        padding-bottom: 20px;
    }
    
    /* H2: Subtitle */
    .book-article h2, .chapter-subtitle {
        font-family: var(--font-ui);
        color: var(--text-secondary);
        margin-top: 1rem; 
        margin-bottom: 2rem;
        font-weight: 300;
        font-size: 18px;
        display: block;
        text-align: center;
    }
    
    /* H3: Section Title */
    .book-article h3 {
        font-family: var(--font-ui);
        color: var(--accent-blue);
        margin-top: 50px;
        font-weight: 600;
        font-size: 1.4rem;
        border-left: 3px solid var(--accent-blue);
        padding-left: 15px;
    }

    .book-paragraph, .book-article p { 
        font-family: var(--font-body);
        font-size: 19px;
        line-height: 1.8;
        color: #d1d1d1;
        margin-bottom: 28px;
        text-align: justify;
    }

    /* Bold Subtopics in Sections */
    .book-article p strong {
        color: #fff;
        font-weight: 700;
    }
    
    /* Verse / Quote System */
    .verse, .book-quote {
        font-style: italic;
        margin: 30px 50px;
        color: var(--accent-blue);
        border-left: 3px solid var(--accent-blue);
        padding-left: 25px;
        font-family: var(--font-body);
        font-size: 19px;
        line-height: 1.8;
    }
    
    .highlight-verse, blockquote {
        text-align: center;
        font-size: 22px;
        font-weight: 300;
        color: #fff;
        margin: 50px 0;
        font-style: italic;
        border: none;
        padding: 0;
    }

    /* Poetic Notes */
    .poetic-note {
        border: 1px solid rgba(157, 78, 221, 0.3);
        background: rgba(157, 78, 221, 0.05);
        padding: 30px;
        margin: 50px 0;
        border-radius: 4px;
        position: relative;
    }
    
    .poetic-note::before {
        content: 'Nota Poética';
        position: absolute;
        top: -12px;
        left: 20px;
        background: var(--bg-content); 
        padding: 0 10px;
        font-family: var(--font-ui);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--accent-purple);
    }

    .poetic-note p {
        margin-bottom: 0.5rem;
        font-style: italic;
        text-align: center;
        color: #e0d0f0;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .book-sidebar {
            position: absolute;
            height: 100%;
            transform: translateX(0);
        }
        .book-sidebar.collapsed {
            transform: translateX(-100%);
            margin-left: 0;
        }
        .book-content-wrapper { padding: 20px; }
    }
</style>
"""

# Icons as simple SVGs
ICON_MENU = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
# Updated Left Icon / Close Icon based on User preference (Arrow Left)
ICON_LEFT = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>'
ICON_HOME = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'

def clean_text(text):
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        if line.strip().isdigit(): continue 
        if "......." in line: continue
        cleaned.append(line)
    return "\n".join(cleaned)

def extract_content(full_text):
    # Regex Patterns for Big Bang
    markers = [
        ("prologo", "Prólogo", "O Grande Teatro da Realidade", r"Prólogo\s+O Grande Teatro"),
        ("apresentacao", "Apresentação", "Um Convite à Jornada Cósmica", r"Apresentação\s+Um Convite"),
    ]
    
    for i in range(1, 44):
        markers.append((f"cap{i:02d}", f"Capítulo {i:02d}", "", fr"Capítulo {i:02d}"))

    markers.append(("conclusao", "Conclusão Final", "Encerramento", r"Encerramento\s+A\s+.ltima|Reflexões Finais\s+O Último Sussurro|Conclusão Final"))
    
    extracted_data = {}
    start_search_idx = full_text.find("Introdução", 500)
    if start_search_idx == -1: start_search_idx = 0
    
    current_idx = start_search_idx
    positions = []
    
    for i, (fname, title, sub, pattern) in enumerate(markers):
        match = re.search(pattern, full_text[current_idx:], re.IGNORECASE)
        real_start = -1
        if match:
             candidate_idx = current_idx + match.start()
             snippet = full_text[candidate_idx : candidate_idx+200]
             if "..." in snippet or ".." in snippet:
                 match2 = re.search(pattern, full_text[candidate_idx+100:], re.IGNORECASE)
                 if match2:
                     real_start = candidate_idx + 100 + match2.start()
                 else:
                     real_start = candidate_idx
             else:
                 real_start = candidate_idx
        
        if real_start != -1:
            positions.append((fname, title, sub, real_start))
            current_idx = real_start + 1
        else:
            positions.append((fname, title, sub, current_idx))

    for i in range(len(positions)):
        fname, title, sub, start = positions[i]
        end = positions[i+1][3] if i < len(positions)-1 else len(full_text)
        
        if end <= start:
            content = "<p>Conteúdo não localizado automaticamente.</p>"
        else:
            raw_content = full_text[start:end]
            content = clean_text(raw_content)
        
        extracted_data[fname] = (title, sub, content)
        
    return extracted_data

def parse_structured_content(text, chapter_id="", title="", subtitle=""):
    lines = text.split('\n')
    output_html = ""
    subsections = []
    
    buffer = [] 
    
    def norm(s): return re.sub(r'\W+', '', s).lower()
    ignore_set = {norm(title), norm(subtitle), norm(title.replace("Capítulo", "").strip())}
    if "cap" in chapter_id:
        ignore_set.add(chapter_id.replace("cap", ""))

    def flush_buffer():
        nonlocal buffer, output_html
        if not buffer: return
        p_text = " ".join(buffer).strip()
        
        if norm(p_text) in ignore_set:
            buffer = []
            return
            
        if p_text:
            if (p_text.startswith('“') and p_text.endswith('”')) or (p_text.startswith('"') and p_text.endswith('"')):
                 output_html += f'<div class="book-quote">{p_text}</div>'
            else:
                 output_html += f'<p class="book-paragraph">{p_text}</p>'
        buffer = []

    i = 0
    passed_header_zone = False 
    
    while i < len(lines):
        line = lines[i].strip()
        if not line: 
            flush_buffer()
            i += 1
            continue
            
        if not passed_header_zone:
            if norm(line) in ignore_set or norm(line) in norm(title):
                i += 1
                continue
            if len(output_html) > 500: passed_header_zone = True

        match_sec = re.match(r"^(Seção \d+(\.\d+)?|Introdução|Reflexões Finais|Conceitos Fundamentais)(.*)", line, re.IGNORECASE)
        match_note = re.match(r"^(Nota Poética|Nota Poética Final)[:\s]*(.*)", line, re.IGNORECASE)
        
        if match_sec:
            flush_buffer()
            passed_header_zone = True
            full_title = match_sec.group(0)
            safe_id = f"{chapter_id}-sec-{len(subsections)}"
            subsections.append((safe_id, full_title))
            output_html += f'<h3 id="{safe_id}">{full_title}</h3>'
            
            if i+1 < len(lines) and len(lines[i+1]) < 100 and lines[i+1].strip():
                 output_html += f'<p class="book-paragraph"><strong>{lines[i+1].strip()}</strong></p>'
                 i += 1
                 
        elif match_note:
            flush_buffer()
            passed_header_zone = True
            note_content = [match_note.group(2)] if match_note.group(2) else []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line:
                     pass
                if re.match(r"^(Seção|Introdução|Nota Poética)", next_line, re.IGNORECASE):
                    i -= 1 
                    break
                note_content.append(next_line)
                i += 1
            
            note_text = " ".join([l for l in note_content if l])
            if note_text:
                output_html += f'<div class="poetic-note"><p>{note_text}</p></div>'
            continue 

        else:
            match_bold = re.match(r"^([A-Z][a-zA-Z0-9\s]+):(.*)", line)
            if match_bold and len(match_bold.group(1)) < 50:
                 flush_buffer()
                 passed_header_zone = True
                 output_html += f'<p class="book-paragraph"><strong>{match_bold.group(1)}:</strong> {match_bold.group(2)}</p>'
            else:
                 buffer.append(line)
        
        i += 1
        
    flush_buffer()
    return output_html, subsections

def generate_full_sidebar_html(structure_data):
    html = '<nav class="sidebar-content"><a href="../index.html" class="toc-item">← Voltar ao Menu</a>'
    
    for part_name, chapters in structure_data:
        if part_name:
            html += f'<div class="toc-group-title">{part_name}</div>'
        
        for ch_id, ch_title, subs in chapters:
            html += f'<a href="#{ch_id}" class="toc-item">{ch_title}</a>'
            for sub_id, sub_title in subs:
                 if "Nota Poética" not in sub_title:
                    html += f'<a href="#{sub_id}" class="toc-item toc-sublink">{sub_title}</a>'
                    
    html += '</nav>'
    return html

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    try:
        doc = fitz.open(PDF_PATH)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    data = extract_content(full_text)
    
    manual_overrides = {
        "prologo": (1, 1),
        "apresentacao": (2, 3), 
        "conclusao": (946, 949)
    }

    for fname, (start_idx, end_idx) in manual_overrides.items():
        if fname in data:
            title, sub, _ = data[fname]
            manual_text = get_text_from_pages(doc, start_idx, end_idx)
            cleaned_manual = clean_text(manual_text)
            data[fname] = (title, sub, cleaned_manual)
            print(f"Overwrote {fname} from pages {start_idx+1}-{end_idx+1}")

    structure_map = [
        ("Intro", ["prologo", "apresentacao"]),
        ("Parte I - A Origem", ["cap01"]),
        ("Parte II - A Escala", [f"cap{i:02d}" for i in range(2, 9)]),
        ("Parte III - A Luz", [f"cap{i:02d}" for i in range(9, 13)]),
        ("Parte IV - A Forja", [f"cap{i:02d}" for i in range(13, 16)]),
        ("Parte V - O Sistema", [f"cap{i:02d}" for i in range(16, 18)]),
        ("Parte VI - A Vida", [f"cap{i:02d}" for i in range(18, 23)]),
        ("Parte VII - A Explosão", [f"cap{i:02d}" for i in range(23, 29)]),
        ("Parte VIII - A Mente", [f"cap{i:02d}" for i in range(29, 32)]),
        ("Parte IX - O Futuro", [f"cap{i:02d}" for i in range(32, 34)]),
        ("Parte X - O Fim", [f"cap{i:02d}" for i in range(34, 40)]),
        ("Parte XI - O Retorno", [f"cap{i:02d}" for i in range(40, 44)]),
        ("Encerramento", ["conclusao"])
    ]

    final_content_html = ""
    sidebar_data = [] 

    keys_order = list(data.keys())

    for part_name, ch_keys in structure_map:
        chapters_data = []
        for ch_key in ch_keys:
            if ch_key not in data: continue
            
            title, subtitle, raw = data[ch_key]
            
            processed_html, subsections = parse_structured_content(raw, ch_key, title, subtitle)
            
            header_html = ""
            if "cap" in ch_key:
                cap_num = title.replace("Capítulo", "").strip()
                header_html = f"""
                <h4 class="structure-label">Capítulo {cap_num}</h4>
                <h1 class="chapter-title">{title}</h1>
                {f'<span class="chapter-subtitle">{subtitle}</span>' if subtitle else ''}
                """
            else:
                header_html = f"""
                <h1 class="main-title">{title}</h1>
                {f'<span class="chapter-subtitle">{subtitle}</span>' if subtitle else ''}
                """

            article_html = f"""
            <article class="book-article" id="{ch_key}">
                <header class="chapter-header">
                    {header_html}
                </header>
                {processed_html}
            </article>
            """
            
            final_content_html += article_html
            chapters_data.append((ch_key, title, subsections))
            
        sidebar_data.append((part_name, chapters_data))

    sidebar_html = generate_full_sidebar_html(sidebar_data)

    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Big Bang - A Grande História</title>
    {CSS_STYLES}
</head>
<body>
    <div class="book-container">
        <!-- Sidebar -->
        <aside class="book-sidebar" id="sidebar">
            <div class="sidebar-header">
                <span class="sidebar-title">Conteúdo</span>
                <button class="toolbar-btn" onclick="toggleSidebar()" title="Fechar Menu">
                    {ICON_LEFT}
                </button>
            </div>
            {sidebar_html}
        </aside>

        <!-- Main Content -->
        <main class="book-main">
            <header class="reader-toolbar">
                <div style="display:flex; gap:10px; align-items:center;">
                    <button class="toolbar-btn" onclick="toggleSidebar()" title="Menu">
                        {ICON_MENU}
                    </button>
                    <a href="../index.html" class="toolbar-btn" title="Home">
                        {ICON_HOME}
                    </a>
                </div>
                
                <span class="toolbar-title">Big Bang - A Grande História</span>

                <div style="width: 70px;"></div>
            </header>

            <div class="book-content-wrapper">
                {final_content_html}
                
                <footer class="reader-footer" style="margin-top: 100px; justify-content: center;">
                    <span style="color: var(--text-muted);">Fim da Jornada</span>
                </footer>
            </div>
        </main>
    </div>

    <script>
        function toggleSidebar() {{
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('collapsed');
        }}
    </script>
</body>
</html>"""

    output_path = os.path.join(OUTPUT_DIR, "bigbang.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated Single Page Book at: {output_path}")

def get_text_from_pages(doc, start_idx, end_idx):
    text = ""
    try:
        for i in range(start_idx, end_idx + 1):
            if i < len(doc):
                text += doc[i].get_text()
    except Exception as e:
        print(f"Error extracting pages {start_idx}-{end_idx}: {e}")
    return text

if __name__ == "__main__":
    main()
