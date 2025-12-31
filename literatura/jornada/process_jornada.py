
import os
import re

JORNADA_PATH = r"e:\Desenvolvimento\universecode\literatura\jornada.html"
BACKUP_PATH = r"e:\Desenvolvimento\universecode\literatura\jornada.html.bak"

def main():
    if not os.path.exists(JORNADA_PATH):
        print(f"File not found: {JORNADA_PATH}")
        return

    # Create backup
    with open(JORNADA_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open(BACKUP_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Backup created.")

    # 1. Inject Timeline Structure
    # We look for <div class="book-container"> and prepending the timeline elements
    # Or actually, we can put it outside book-container or inside. 
    # Let's put it as a direct child of body or just before book-main if possible.
    # The user request said "Adicionar botão de Timeline na toolbar" and "Adicionar container...".
    
    # HTML for Timeline Overlay/Sidebar
    timeline_html = """
    <!-- Timeline Interativa -->
    <div id="timeline-overlay" class="timeline-overlay" onclick="closeTimeline()"></div>
    <aside id="timeline-sidebar" class="timeline-sidebar">
        <div class="timeline-header">
            <span class="timeline-title">Linha Temporal</span>
            <button class="close-timeline-btn" onclick="closeTimeline()">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
        </div>
        <div id="timeline-content-area" class="timeline-content">
            <!-- Items injected by JS -->
        </div>
    </aside>
    """

    if 'id="timeline-sidebar"' not in content:
        # Inject right after <body>
        content = content.replace('<body>', '<body>\n' + timeline_html)
        print("Timeline HTML injected.")

    # 2. Inject CSS and JS imports
    css_import = '<link href="jornada/timeline.css" rel="stylesheet" />'
    js_import = '<script src="jornada/timeline.js"></script>'

    if 'timeline.css' not in content:
        content = content.replace('</head>', f'    {css_import}\n</head>')
    
    if 'timeline.js' not in content:
        content = content.replace('</body>', f'    {js_import}\n</body>')

    print("Resources imported.")

    # 3. Add Timeline Button to Toolbar
    # Search for the toolbar div
    # <header class="reader-toolbar">
    #    <div style="display:flex; gap:10px; align-items:center;">
    #        <button class="toolbar-btn" onclick="toggleSidebar()" ...
    
    timeline_btn = """
                    <button class="toolbar-btn" onclick="toggleTimeline()" title="Timeline Cósmica">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    </button>
    """

    if 'toggleTimeline()' not in content:
        # We insert it after the toggleSidebar button
        # The pattern is specific to the file content we saw
        pattern = r'(<button class="toolbar-btn" onclick="toggleSidebar\(\)" title="Menu">[\s\S]*?</button>)'
        match = re.search(pattern, content)
        if match:
            # Insert after the match
            content = content[:match.end()] + timeline_btn + content[match.end():]
            print("Timeline button injected.")
        else:
            print("Warning: Could not find sidebar button to insert timeline button after.")

    # 4. Inject Images into Chapters
    # Need to match <article ... id="capX"> ... <header class="chapter-header"> ... </header>
    # And insert <img src="jornada/cap_XX.png" ...>
    
    # Improved Regex to find article headers and inject image if not already present
    # Using a callback function for substitution to handle dynamic image names
    
    def inject_image(match):
        full_match = match.group(0)
        article_id = match.group(1)
        header_content = match.group(2)
        
        # Determine image filename
        if article_id == 'conclusao':
            img_name = 'cap_44.png'
        elif article_id.startswith('cap'):
            try:
                num = int(article_id.replace('cap', ''))
                img_name = f'cap_{num:02d}.png'
            except ValueError:
                return full_match
        else:
            return full_match
            
        img_tag = f'\n                    <img src="jornada/{img_name}" class="chapter-cover-img" alt="Capa do Capítulo" style="width:100%; height:auto; border-radius:8px; margin-top:20px; margin-bottom:20px; box-shadow:0 4px 15px rgba(0,0,0,0.5); object-fit: cover; max-height: 350px;">'
        
        # Check if image is already there
        if 'class="chapter-cover-img"' in full_match:
            return full_match
        
        return f'<article class="book-article" id="{article_id}">\n{header_content}{img_tag}'

    # Pattern explanation:
    # <article class="book-article" id="([^"]+)"> matches opening tag and captures ID
    # (\s*<header class="chapter-header">[\s\S]*?</header>) matches the header block
    pattern = r'<article class="book-article" id="([^"]+)">(\s*<header class="chapter-header">[\s\S]*?</header>)'
    
    content = re.sub(pattern, inject_image, content)
    print("Images injected.")

    with open(JORNADA_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("File updated successfully.")

if __name__ == "__main__":
    main()
