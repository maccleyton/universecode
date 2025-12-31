import os
import re

BASE_DIR = r"e:\Desenvolvimento\universecode\literatura"
JORNADA_FILE = os.path.join(BASE_DIR, "jornada.html")
OUTPUT_DIR = os.path.join(BASE_DIR, "jornada")
INDEX_OUTPUT = JORNADA_FILE

# Template for individual chapters (Big Bang style)
CHAPTER_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - A Grande Jornada do Cosmos</title>
    <link href="../style.css" rel="stylesheet" />
    <link href="./timeline.css" rel="stylesheet" />
</head>
<body>
    <div class="book-container">
        <!-- Sidebar -->
        <aside class="book-sidebar" id="sidebar">
            <div class="sidebar-header">
                <span class="sidebar-title">Sumário</span>
                <button class="toolbar-btn" onclick="toggleSidebar()" title="Fechar Menu">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
                </button>
            </div>
            <nav class="sidebar-content">
                <a href="../jornada.html" class="toc-item">← Voltar ao Índice</a>
                {sidebar_links}
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="book-main">
            <header class="reader-toolbar">
                <div style="display:flex; gap:10px; align-items:center;">
                    <button class="toolbar-btn" onclick="toggleSidebar()" title="Menu">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="4" x2="20" y1="12" y2="12" />
                            <line x1="4" x2="20" y1="6" y2="6" />
                            <line x1="4" x2="20" y1="18" y2="18" />
                        </svg>
                    </button>
                    <!-- Home Button -->
                    <a href="../index.html" class="toolbar-btn" title="Home">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
                            <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                            <polyline points="9 22 9 12 15 12 15 22" />
                        </svg>
                    </a>
                </div>

                <div class="toolbar-navigation" style="display:flex; align-items:center; gap:15px;">
                    {prev_btn}
                    <span class="toolbar-title">A Grande Jornada do Cosmos</span>
                    {next_btn}
                </div>

                <div style="width: 70px;"></div>
            </header>

            <div class="book-content-wrapper">
                <article class="book-article">
                    {content}
                </article>
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

# Template for the Timeline Index (Jornada Home)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Grande Jornada do Cosmos - Timeline</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-app: #000000;
            --bg-card: #1e1e1e;
            --text-primary: #e0e0e0;
            --text-secondary: #a0a0a0;
            --accent-color: #3a86ff; /* Azul Original */
            --border-subtle: 1px solid rgba(255, 255, 255, 0.1);
            --font-ui: 'Inter', sans-serif;
            --font-body: 'Merriweather', serif;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-app);
            background: radial-gradient(circle at 50% 20%, #1a1a1a 0%, #000000 80%);
            background-attachment: fixed;
            color: var(--text-primary);
            font-family: var(--font-ui);
            min-height: 100vh;
            overflow-y: auto;
        }}

        /* SCROLLBAR - Big Bang Standard */
        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: var(--bg-app);
            border-left: 1px solid var(--border-subtle);
        }}
        
        ::-webkit-scrollbar-thumb {{
            background-color: #333;
            border-radius: 5px;
            border: 2px solid var(--bg-app);
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background-color: var(--accent-color);
        }}

        /* Header Style from Big Bang */
        #main-toolbar {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 56px;
            background: rgba(0, 0, 0, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            z-index: 1000;
            display: flex;
            align-items: center;
            padding: 0 15px;
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: none;
        }}

        .nav-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            padding: 8px 12px;
            margin-right: 4px;
            border-radius: 6px;
            transition: all 0.2s ease;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .nav-btn:hover {{
            color: var(--accent-color);
            background: rgba(58, 134, 255, 0.1);
            border: 1px solid rgba(58, 134, 255, 0.3);
            box-shadow: 0 0 8px rgba(58, 134, 255, 0.2);
        }}

        .container {{
            max-width: 1000px;
            width: 100%;
            margin: 0 auto;
            padding: 80px 20px 60px;
        }}

        .book-cover {{
            text-align: center;
            margin-bottom: 80px;
            padding-bottom: 40px;
            border-bottom: var(--border-subtle);
        }}

        .main-title {{
            font-family: var(--font-ui);
            font-size: 48px;
            font-weight: 800;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 4px;
            line-height: 1.1;
            margin-bottom: 15px;
        }}

        .sub-title {{
            font-family: var(--font-ui);
            font-size: 24px;
            font-weight: 300;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 30px;
            display: block;
        }}

        .author {{
            font-family: var(--font-body);
            font-size: 20px;
            color: var(--accent-color);
            font-style: italic;
            margin-top: 20px;
        }}

        /* Timeline Styles */
        .timeline-container {{
            position: relative;
            padding: 20px 0;
        }}

        /* Vertical Line */
        .timeline-container::before {{
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, transparent, var(--accent-color), transparent);
            transform: translateX(-50%);
        }}

        .timeline-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 80px;
            position: relative;
            width: 100%;
        }}

        /* Dots on the line */
        .timeline-dot {{
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 16px;
            height: 16px;
            background: #000;
            border: 2px solid var(--accent-color);
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(58, 134, 255, 0.5);
            z-index: 2;
        }}

        .timeline-content {{
            width: 45%;
        }}

        .timeline-item:nth-child(even) {{
            flex-direction: row-reverse;
        }}
        
        .timeline-item:nth-child(even) .timeline-content {{
            text-align: left;
        }}
        
        .timeline-item:nth-child(odd) .timeline-content {{
            text-align: right;
        }}

        /* Chapter Card Style */
        .chapter-card {{
            display: block;
            text-decoration: none;
            background: var(--bg-card);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
        }}

        .chapter-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent-color);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}

        .card-img {{
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}

        .card-info {{
            padding: 20px;
        }}

        .card-num {{
            font-size: 0.8rem;
            color: var(--accent-color);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 700;
            display: block;
            margin-bottom: 8px;
        }}

        .card-title {{
            font-size: 1.4rem;
            color: #fff;
            font-family: var(--font-body);
            font-weight: 700;
            margin-bottom: 8px;
            line-height: 1.3;
        }}

        .card-sub {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            font-family: var(--font-ui);
            font-style: italic;
        }}

        @media (max-width: 768px) {{
            .timeline-container::before {{
                left: 20px;
            }}
            .timeline-item {{
                flex-direction: column;
                align-items: flex-start;
                margin-left: 50px;
                width: auto;
            }}
            .timeline-item:nth-child(even) {{
                flex-direction: column;
            }}
            .timeline-dot {{
                left: 20px;
            }}
            .timeline-content {{
                width: 100%;
                text-align: left !important;
            }}
        }}
    </style>
</head>
<body>
    <nav id="main-toolbar">
        <a href="../index.html" class="nav-btn" title="Voltar ao Início">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
        </a>
        {nav_links}
    </nav>

    <div class="container">
        <header class="book-cover">
            <h1 class="main-title">A Grande Jornada do Cosmos</h1>
            <span class="sub-title">Do Big Bang à Consciência</span>
            <div class="author">Cleyton D. Macedo</div>
        </header>

        <div class="timeline-container">
            {cards}
        </div>
    </div>
</body>
</html>"""

def get_nav_btn(href, title, direction):
    if not href:
        return '<div style="width: 24px;"></div>' # Spacer
    
    icon = '<polyline points="15 18 9 12 15 6"></polyline>' if direction == 'prev' else '<polyline points="9 18 15 12 9 6"></polyline>'
    
    return f"""
    <a href="{href}" class="nav-chevron" title="{title}">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            {icon}
        </svg>
    </a>
    """

def process_chapters():
    if not os.path.exists(JORNADA_FILE):
        print(f"File not found: {JORNADA_FILE}")
        return

def rebuild_index():
    print("Rebuilding index from existing chapter files...")
    chapters = []
    
    # List all html files in jornada/
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith('.html')]
    
    for filename in files:
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse metadata
        num_match = re.search(r'<span class="chapter-number">([^<]+)</span>', content)
        title_match = re.search(r'<h1 class="chapter-title">([^<]+)</h1>', content)
        sub_match = re.search(r'<span class="chapter-sub">([^<]+)</span>', content)
        img_match = re.search(r'<img src="([^"]+)"', content)
        
        number = num_match.group(1) if num_match else ""
        title = title_match.group(1) if title_match else "Sem Título"
        subtitle = sub_match.group(1) if sub_match else ""
        img_src = img_match.group(1) if img_match else "" # This will be relative to the chapter file (e.g. "cap_01.png")
        
        # Sort key
        if filename == 'conclusao.html':
            num_int = 999
        else:
            try:
                num_int = int(re.search(r'capitulo_(\d+)', filename).group(1))
            except:
                num_int = 0
                
        chapters.append({
            'filename': filename,
            'number': number,
            'title': title,
            'subtitle': subtitle,
            'image': img_src,
            'num_int': num_int
        })
        
    # Sort chapters
    chapters.sort(key=lambda x: x['num_int'])
    
    # Generate Index HTML
    cards_html = ""
    nav_links_html = ""
    
    chunk_size = 10
    total_chapters = len(chapters)
    num_chunks = (total_chapters // chunk_size) + (1 if total_chapters % chunk_size > 0 else 0)

    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, total_chapters)
        
        if start >= total_chapters: break

        start_num = chapters[start]['num_int']
        end_num = chapters[end-1]['num_int']
        
        if start_num == 999: label = "Fim"
        elif end_num == 999: label = f"{start_num}-Fim"
        else: label = f"{start_num}-{end_num}"
        
        nav_links_html += f'<a href="#group-{i}" class="nav-btn">{label}</a>\n'

    for i, chapter in enumerate(chapters):
        group_id = ""
        if i % chunk_size == 0:
            group_idx = i // chunk_size
            group_id = f'id="group-{group_idx}"'
            
        cards_html += f"""
        <div class="timeline-item" {group_id}>
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <a href="jornada/{chapter['filename']}" class="chapter-card">
                    <img src="jornada/{chapter['image']}" alt="Capa" class="card-img">
                    <div class="card-info">
                        <span class="card-num">{chapter['number']}</span>
                        <div class="card-title">{chapter['title']}</div>
                        <div class="card-sub">{chapter['subtitle']}</div>
                    </div>
                </a>
            </div>
        </div>
        """

    index_html = INDEX_TEMPLATE.format(cards=cards_html, nav_links=nav_links_html)
    with open(INDEX_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"Index rebuilt at {INDEX_OUTPUT}")

def process_chapters():
    # Check if we should split (source exists and looks like the monolithic file) or rebuild
    # Since we overwrote it, we likely need to rebuild.
    # But let's check if the file contains "timeline-container" (meaning it is the index)
    should_rebuild = False
    
    if os.path.exists(JORNADA_FILE):
        with open(JORNADA_FILE, 'r', encoding='utf-8') as f:
            if 'timeline-container' in f.read():
                should_rebuild = True
    else:
        should_rebuild = True

    if should_rebuild:
        rebuild_index()
        return

    # ... Original splitting logic ...
    # (Leaving this here in case we restore the file, but practically we will hit rebuild)
    # For now, just call rebuild logic directly or comment out the rest.
    
    print("WARNING: Original logic skipped, assuming rebuild needed.")
    rebuild_index()

    # if not os.path.exists(JORNADA_FILE):
    #     print(f"File not found: {JORNADA_FILE}")
    #     return

    # with open(JORNADA_FILE, 'r', encoding='utf-8') as f:
    #     content = f.read()

    # # Regex to find articles
    # # Assumes injected images are present inside the article or header
    # # But based on my previous injection, the image is INSIDE the article, AFTER the header.
    # # Pattern: <article ... id="capX"> ... </article>
    
    # article_pattern = re.compile(r'<article class="book-article" id="([^"]+)">([\s\S]*?)</article>')
    # matches = list(article_pattern.finditer(content))
    
    # chapters = []
    
    # print(f"Found {len(matches)} articles.")

    # for i, match in enumerate(matches):
    #     art_id = match.group(1)
    #     art_content = match.group(2)
        
    #     # Extract metadata
    #     num_match = re.search(r'<span class="chapter-number">([^<]+)</span>', art_content)
    #     title_match = re.search(r'<h1 class="chapter-title">([^<]+)</h1>', art_content)
    #     sub_match = re.search(r'<span class="chapter-sub">([^<]+)</span>', art_content)
    #     img_match = re.search(r'<img src="([^"]+)"', art_content)
        
    #     number = num_match.group(1) if num_match else ""
    #     title = title_match.group(1) if title_match else "Sem Título"
    #     subtitle = sub_match.group(1) if sub_match else ""
    #     img_src = img_match.group(1) if img_match else ""
        
    #     # Normalize Image Path for subfolder usage
    #     # Original: jornada/cap_XX.png
    #     # New location: jornada/capitulo_XX.html -> image is in ./cap_XX.png (same folder)
    #     # So we strip 'jornada/' prefix
    #     if img_src.startswith('jornada/'):
    #         img_src = img_src.replace('jornada/', '')
        
    #     # Determine filename
    #     if art_id == 'conclusao':
    #         filename = 'conclusao.html'
    #         num_int = 43 # Treating conclusion as 43
    #     else:
    #         try:
    #             num_int = int(art_id.replace('cap', ''))
    #             filename = f'capitulo_{num_int:02d}.html'
    #         except:
    #             filename = f'{art_id}.html'
    #             num_int = 999

    #     chapters.append({
    #         'id': art_id,
    #         'filename': filename,
    #         'number': number,
    #         'title': title,
    #         'subtitle': subtitle,
    #         'image': img_src,
    #         'content': art_content,
    #         'num_int': num_int
    #     })

    # # Generate Sidebar Links (Shared)
    # sidebar_links = ""
    # for ch in chapters:
    #     sidebar_links += f'<a href="{ch["filename"]}" class="toc-item">{ch["number"]}. {ch["title"]}</a>\n'

    # # Generate Files
    # cards_html = ""
    # nav_links_html = ""
    
    # # Create Navigation Groups (chunks of 10)
    # chunk_size = 10
    # total_chapters = len(chapters)
    # num_chunks = (total_chapters // chunk_size) + (1 if total_chapters % chunk_size > 0 else 0)

    # for i in range(num_chunks):
    #     start = i * chunk_size
    #     end = min((i + 1) * chunk_size, total_chapters)
        
    #     # Find start and end chapter numbers for label
    #     start_num = chapters[start]['num_int']
    #     end_num = chapters[end-1]['num_int']
        
    #     # Handle special cases (like Conclusao being 999/43)
    #     if start_num == 999: label = "Fim"
    #     elif end_num == 999: label = f"{start_num}-Fim"
    #     else: label = f"{start_num}-{end_num}"
        
    #     nav_links_html += f'<a href="#group-{i}" class="nav-btn">{label}</a>\n'

    # for i, chapter in enumerate(chapters):
    #     # Determine if this starts a new group
    #     group_id = ""
    #     if i % chunk_size == 0:
    #         group_idx = i // chunk_size
    #         group_id = f'id="group-{group_idx}"'

    #     prev_ch = chapters[i-1] if i > 0 else None
    #     next_ch = chapters[i+1] if i < len(chapters)-1 else None
        
    #     prev_btn = get_nav_btn(prev_ch['filename'], "Anterior", "prev") if prev_ch else get_nav_btn("", "", "prev")
    #     next_btn = get_nav_btn(next_ch['filename'], "Próximo", "next") if next_ch else get_nav_btn("", "", "next")

    #     fixed_content = chapter['content'].replace('src="jornada/', 'src="')
        
    #     html = CHAPTER_TEMPLATE.format(
    #         title=chapter['title'],
    #         sidebar_links=sidebar_links,
    #         prev_btn=prev_btn,
    #         next_btn=next_btn,
    #         content=fixed_content
    #     )
        
    #     out_path = os.path.join(OUTPUT_DIR, chapter['filename'])
    #     with open(out_path, 'w', encoding='utf-8') as f:
    #         f.write(html)
            
    #     print(f"Generated {out_path}")
        
    #     # Vertical Timeline Card HTML
    #     cards_html += f"""
    #     <div class="timeline-item" {group_id}>
    #         <div class="timeline-dot"></div>
    #         <div class="timeline-content">
    #             <a href="jornada/{chapter['filename']}" class="chapter-card">
    #                 <img src="jornada/{chapter['image']}" alt="Capa" class="card-img">
    #                 <div class="card-info">
    #                     <span class="card-num">{chapter['number']}</span>
    #                     <div class="card-title">{chapter['title']}</div>
    #                     <div class="card-sub">{chapter['subtitle']}</div>
    #                 </div>
    #             </a>
    #         </div>
    #     </div>
    #     """

    # index_html = INDEX_TEMPLATE.format(cards=cards_html, nav_links=nav_links_html)
    # with open(INDEX_OUTPUT, 'w', encoding='utf-8') as f:
    #     f.write(index_html)
    
    # print(f"Index generated at {INDEX_OUTPUT}")

if __name__ == "__main__":
    process_chapters()
