
import fitz

def debug_start():
    doc = fitz.open("bigbang.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
        if len(text) > 5000: break
    
    print("--- START TEXT ---")
    print(text[:5000])
    print("--- END TEXT ---")

if __name__ == "__main__":
    debug_start()
