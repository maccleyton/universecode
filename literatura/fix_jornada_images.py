import os
import re

BASE_DIR = r"e:\Desenvolvimento\universecode\literatura\jornada"

def fix_chapter_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the image INSIDE the article (usually after the header)
    # The current structure in jornada/cap01.html:
    # <article class="book-article">
    #    <header ...>...</header>
    #    <img src="..." class="chapter-cover-img" ...>
    
    # We want to extract that image and move it BEFORE <article class="book-article">
    # And change class to "chapter-cover-image" and remove inline styles.

    # Regex to capture the Image Tag attributes
    img_pattern = re.compile(r'(<article class="book-article">[\s\S]*?)<img src="([^"]+)"[^>]*>(?:[\s\S]*?)(?=<p|<div)', re.MULTILINE)
    
    # This regex is tricky because the image might be anywhere.
    # Let's try a simpler approach: Find the image tag, extract src. Remove it. Insert new tag before article.
    
    # 1. Find the specific cover image (usually class="chapter-cover-img")
    cover_match = re.search(r'<img src="([^"]+)" class="chapter-cover-img"[^>]*>', content)
    
    if not cover_match:
        # Try to find without class if needed, or maybe it's already fixed?
        # print(f"No cover image found in {os.path.basename(filepath)}")
        return False
        
    img_src = cover_match.group(1)
    full_tag = cover_match.group(0)
    
    # 2. Remove the old tag
    new_content = content.replace(full_tag, '')
    
    # 3. Create new tag
    # Using the user's restored class: chapter-cover-image
    # And ensuring it's outside the article.
    # Ideally before <article class="book-article">
    
    new_tag = f'\n<img src="{img_src}" class="chapter-cover-image" alt="Capa Capítulo">\n'
    
    # Insert before article
    if '<article class="book-article">' in new_content:
        new_content = new_content.replace('<article class="book-article">', f'{new_tag}<article class="book-article">')
        print(f"Fixed {os.path.basename(filepath)}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    else:
        print(f"Article tag not found in {os.path.basename(filepath)}")
        return False

def main():
    if not os.path.exists(BASE_DIR):
        print(f"Dir not found: {BASE_DIR}")
        return

    files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    count = 0
    for file in files:
        if fix_chapter_file(os.path.join(BASE_DIR, file)):
            count += 1
            
    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    main()
