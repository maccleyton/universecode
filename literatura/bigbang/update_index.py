
import re
import os

INDEX_PATH = r"e:\Desenvolvimento\universecode\literatura\bigbang\index.html"

def update_index():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Part Backgrounds (Handle remaining ones)
    # Mapping logic: default "imagens/parteX_bg.jpg" -> "assets/part_0X.jpg"
    # Note: user might have different naming.
    # We'll just replace "imagens/parte(\d+)_bg.jpg" with "assets/part_\1.jpg" generically
    # and fix numbering formatting if needed.
    
    def repl_part_bg(m):
        num = m.group(1) # '1', '2', etc.
        try:
            n = int(num)
            return f"assets/part_{n:02d}.jpg"
        except:
            return f"assets/part_{num}.jpg"

    content = re.sub(r"imagens/parte(\d+)_bg\.jpg", repl_part_bg, content)
    content = re.sub(r"imagens/parte(\d+)_bg\.jpg", repl_part_bg, content) # Case safety?

    # Update Chapter Links and add Styles
    # Regex to find <a href="capitulo_X.html" class="chapter-card"> ... 
    # and replace with <a href="capitulos/capitulo_X.html" class="chapter-card" style="bg-image...">
    
    def repl_chap_card(m):
        href_file = m.group(1) # capitulo_02.html
        
        # Check if already has style
        full_match = m.group(0)
        if "style=" in full_match:
            return full_match # Already processed or valid
        
        # Extract number for image
        # href could be "capitulo_02.html" -> cap_02.jpg
        # href could be "prologo.html" -> cap_prologo?? No, specific handling needed?
        # User said "Subcards dos Capítulos devem ter background-image: url('assets/cap_X.jpg')"
        # Prólogo/Apresentação/Conclusão might need "assets/cap_prologo.jpg" etc?
        # But I only have C01-C43.
        # I will handle numbered chapters specifically.
        
        num_match = re.search(r"capitulo_(\d+)", href_file)
        if num_match:
            num = int(num_match.group(1))
            img_name = f"assets/cap_{num:02d}.jpg"
            new_href = f"capitulos/{href_file}"
            return f'<a href="{new_href}" class="chapter-card" style="background-image: url(\'{img_name}\');">'
        
        # Handle special files (prologo, etc) - Update HREF only if no number
        if "capitulos/" not in href_file:
             return f'<a href="capitulos/{href_file}" class="chapter-card">'
        
        return full_match

    # Use regex that captures the opening tag of link
    content = re.sub(r'<a href="([^"]+)" class="chapter-card[^>]*>', repl_chap_card, content)

    # Fix specific special cases if not handled by generic regex for images
    # Prólogo, Apresentação, Conclusão: Maybe no image or specific one?
    # I'll leave them without image for now unless I find mapped assets.
    
    # Also fix explicit Part 3 to 11 if regex failed due to "imagens/parte3_bg.jpg" pattern match.
    # My regex `imagens/parte(\d+)_bg\.jpg` should catch `imagens/parte3_bg.jpg`.
    
    # Fix Part 10 and 11 specifically just in case
    content = content.replace("imagens/parte10_bg.jpg", "assets/part_10.jpg")
    content = content.replace("imagens/parte11_bg.jpg", "assets/part_11.jpg")
    content = content.replace("imagens/part_00.jpg", "assets/part_intro.jpg") # Rename Intro back if desired or stick to 00
    
    # Fix paths that might have become "capitulos/capitulos/..." if ran twice?
    # No, regex checks.

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Index updated.")

if __name__ == "__main__":
    update_index()
