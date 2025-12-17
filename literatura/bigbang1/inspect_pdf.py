
import fitz

def inspect_pdf():
    try:
        doc = fitz.open("bigbang.pdf")
        print(f"Total pages: {len(doc)}")
        
        # Print first few pages to understand Prologue/Intro
        print("\n--- PAGE 1-10 ---")
        for i in range(10):
            if i < len(doc):
                print(f"--- PAGE {i+1} START ---")
                print(doc[i].get_text())
                print(f"--- PAGE {i+1} END ---")
        
        # Search for "Capítulo 1" to see how it looks
        print("\n--- SEARCHING CHAPTERS ---")
        for i, page in enumerate(doc):
            text = page.get_text()
            if "Capítulo 1" in text or "CAPÍTULO 1" in text:
                print(f"Found Chapter 1 candidate on page {i+1}")
                print(text[:500])
                break
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_pdf()
