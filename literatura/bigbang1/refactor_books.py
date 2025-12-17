import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Adjust logic to find input files in the parent directory 'literatura'
# Since this script is likely in 'literatura/bigbang' or 'literatura' depending on where I run it.
# The files are at e:\Desenvolvimento\universecode\literatura\jornada.html
# and e:\Desenvolvimento\universecode\literatura\potencial.html
# The script is at e:\Desenvolvimento\universecode\literatura\bigbang\refactor_books.py
# So the paths are ../jornada.html

ROOT_LIT_DIR = os.path.dirname(BASE_DIR) # universecode/literatura
JORNADA_PATH = os.path.join(ROOT_LIT_DIR, "jornada.html")
POTENCIAL_PATH = os.path.join(ROOT_LIT_DIR, "potencial.html")

# --- CSS STYLES (MATCHING BIG BANG) ---
CSS_STYLES = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

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

        /* Dimensões */
        --sidebar-w: 280px;
        --toolbar-h: 50px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; outline: none; }
    
    body {
        background-color: var(--bg-app);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
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
    
    /* Toggle State Class for JS */
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

    /* Main Area */
    .book-main {
        flex: 1;
        display: flex;
        flex-direction: column;
        background: var(--bg-app);
        position: relative;
        min-width: 0; /* Fix flex child overflow */
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
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 1.1rem;
        padding-bottom: 60px;
    }
    
    /* Specific overrides for imported content headers if needed */
    .book-article h1, .chapter-title {
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 2rem;
        border-bottom: 1px solid var(--border-subtle);
        padding-bottom: 20px;
        color: #fff;
    }

    .book-article h2, .book-article h3 { color: var(--accent-blue); margin-top: 2rem; font-weight: 600; }
    
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
    }
</style>
"""

ICONS = {
    "menu": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>',
    "close": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 18 12"/></svg>',
    "home": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
}

def clean_toc_item(line):
    # Converts <a href="..." class="toc-link">...</a> to standard toc-item
    match = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', line)
    if match:
        href, text = match.groups()
        return f'<a href="{href}" class="toc-item">{text}</a>'
    return ""

def refactor_file(path):
    if not os.path.exists(path):
        print(f"File not found: {path} (Checked {path})")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "Livro"

    # 2. Extract TOC
    toc_html = ""
    toc_start = content.find('<ul class="toc-list">')
    if toc_start != -1:
        toc_end = content.find('</ul>', toc_start)
        raw_toc = content[toc_start:toc_end]
        lines = raw_toc.split('\n')
        for line in lines:
            cleaned = clean_toc_item(line)
            if cleaned:
                toc_html += cleaned
    
    # 3. Extract Main Content
    # Using specific markers for these files
    start_tag = '<div class="content-wrapper">'
    start_idx = content.find(start_tag)
    
    if start_idx == -1:
        print(f"Could not find content-wrapper in {path}")
        return
        
    end_main_idx = content.find('</main>')
    if end_main_idx == -1: end_main_idx = content.find('</body>')
    
    raw_inner = content[start_idx + len(start_tag) : end_main_idx]
    # Remove last </div>
    raw_inner = raw_inner.rsplit('</div>', 1)[0]
    
    # 4. Construct New HTML
    new_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {CSS_STYLES}
</head>
<body>
    <div class="book-container">
        <!-- Sidebar -->
        <aside class="book-sidebar" id="sidebar">
            <div class="sidebar-header">
                <span class="sidebar-title">Conteúdo</span>
                <button class="toolbar-btn" onclick="toggleSidebar()" title="Fechar Menu">
                    {ICONS['close']}
                </button>
            </div>
            <nav class="sidebar-content">
                <a href="index.html" class="toc-item">← Voltar ao Menu</a>
                {toc_html}
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="book-main">
            <header class="reader-toolbar">
                <div style="display:flex; gap:10px; align-items:center;">
                    <button class="toolbar-btn" onclick="toggleSidebar()" title="Menu">
                        {ICONS['menu']}
                    </button>
                    <a href="index.html" class="toolbar-btn" title="Home">
                        {ICONS['home']}
                    </a>
                </div>
                
                <span class="toolbar-title">{title}</span>

                <div style="width: 70px;"></div>
            </header>

            <div class="book-content-wrapper">
                {raw_inner}
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

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Updated {path}")

def main():
    print(f"Updating files in {ROOT_LIT_DIR}")
    refactor_file(JORNADA_PATH)
    refactor_file(POTENCIAL_PATH)

if __name__ == "__main__":
    main()
