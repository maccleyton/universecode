
import fitz

def check_pages():
    try:
        doc = fitz.open("literatura/bigbang/bigbang.pdf")
        
        # User said: Prólogo is page 2
        print(f"--- Page 2 (Index 1) ---")
        print(doc[1].get_text()[:500])
        
        # User said: Apresentação is pages 3 and 4
        print(f"\n--- Page 3 (Index 2) ---")
        print(doc[2].get_text()[:500])
        print(f"\n--- Page 4 (Index 3) ---")
        print(doc[3].get_text()[:500])

        # Check end of file for Conclusão/Encerramento (User said 947-950)
        # Note: If PDF has fewer pages, this might error, so checking count first.
        print(f"\nTotal Pages: {len(doc)}")
        
        if len(doc) >= 950:
             print(f"\n--- Page 947 (Index 946) ---")
             print(doc[946].get_text()[:500])
             print(f"\n--- Page 950 (Index 949) ---")
             print(doc[949].get_text()[:500])
        else:
            print("PDF has fewer than 950 pages.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_pages()
