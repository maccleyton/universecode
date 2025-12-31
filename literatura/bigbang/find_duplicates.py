import os
import re
import difflib

# Paths
BASE_DIR = r"e:\Desenvolvimento\universecode\literatura\bigbang"

def normalize_text(text):
    """Removes HTML tags and extra whitespace for comparison."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_content(filename):
    path = os.path.join(BASE_DIR, filename)
    if not os.path.exists(path):
        return None

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Poetic Notes
    # Assuming <div class="poetic-note">...</div>
    # Using regex with DOTALL
    notes_raw = re.findall(r'<div class="poetic-note">(.*?)</div>', content, re.DOTALL)
    notes = [normalize_text(n) for n in notes_raw]

    # Extract Reflexões Finais
    # Locating "Reflexões Finais" and taking subsequent content until end of article or next header?
    # Usually it's the last section.
    # Pattern: <span class="chapter-number">Reflexões Finais</span> ... content ... </article>
    
    reflection = ""
    match_ref = re.search(r'Reflexões Finais</span>(.*?)<div class="verse">', content, re.DOTALL) 
    # Try a broader specific pattern often found in these files
    # The structure often is: Header(Reflexões Finais) -> Title -> Paragraphs -> Verse(Who am I) -> Paragraphs -> Poetic Note -> End.
    
    # Let's try to capture from "Reflexões Finais" to the end of the article, excluding the very last poetic note if possible?
    # Or actually, just capture the whole text block of that section for comparison.
    
    if "Reflexões Finais" in content:
        # Find start position
        start_idx = content.find("Reflexões Finais")
        # Find end of article
        end_idx = content.find("</article>")
        if start_idx != -1 and end_idx != -1:
            raw_section = content[start_idx:end_idx]
            # Clean it up
            reflection = normalize_text(raw_section)
            # Remove the literal "Reflexões Finais" from start
            reflection = reflection.replace("Reflexões Finais", "").strip()

    return {
        'filename': filename,
        'notes': notes,
        'reflection': reflection
    }

def main():
    files = sorted([f for f in os.listdir(BASE_DIR) if f.startswith("capitulo_") and f.endswith(".html")])
    
    data = []
    print(f"Scanning {len(files)} chapters...")
    
    for f in files:
        res = extract_content(f)
        if res:
            data.append(res)

    print("\n--- Analysing Poetic Notes ---")
    # Map note_content -> list of chapters
    note_map = {}
    for entry in data:
        for note in entry['notes']:
            # Use a hash of first 50 chars or full text? Full text.
            if len(note) < 10: continue # Skip very short snippets if any
            if note not in note_map:
                note_map[note] = []
            note_map[note].append(entry['filename'])

    found_dup_notes = False
    for note, chapters in note_map.items():
        if len(chapters) > 1:
            found_dup_notes = True
            print(f"\n[DUPLICATE NOTE FOUND IN {len(chapters)} CHAPTERS]")
            print(f"Chapters: {', '.join(chapters)}")
            print(f"Content snippet: {note[:100]}...")

    if not found_dup_notes:
        print("No exact duplicate poetic notes found.")

    print("\n--- Analysing Final Reflections ---")
    # Comparisons are harder here because they might be long.
    # We will do pairwise comparison? Or grouping.
    
    # Let's map normalized content -> chapters
    ref_map = {}
    for entry in data:
        ref = entry['reflection']
        if len(ref) < 50: continue # Skip empty/short
        
        # We might want fuzzy matching, but let's start with exact (normalized)
        # Using a key based on the first 100 chars to group potential matches?
        # Actually user said "same or repeated parts", let's start with exact logic first.
        
        if ref not in ref_map:
            ref_map[ref] = []
        ref_map[ref].append(entry['filename'])

    found_dup_ref = False
    for ref, chapters in ref_map.items():
        if len(chapters) > 1:
            found_dup_ref = True
            print(f"\n[DUPLICATE REFLECTION FOUND IN {len(chapters)} CHAPTERS]")
            print(f"Chapters: {', '.join(chapters)}")
            print(f"Content snippet: {ref[:100]}...")

    # Also check for High Similarity (e.g. template usage)
    # We can check similarity between all unique reflections
    unique_refs = list(ref_map.keys())
    if len(unique_refs) > 1:
        print("\n[checking for similar reflections...]")
        import itertools
        for r1, r2 in itertools.combinations(unique_refs, 2):
            # SequenceMatcher is slow for huge text, but fine for 40 chapters.
            ratio = difflib.SequenceMatcher(None, r1, r2).ratio()
            if ratio > 0.8: # Threshold for "very similar"
                found_dup_ref = True
                print(f"\n[HIGH SIMILARITY {ratio:.2f}]")
                print(f"Group A: {ref_map[r1]}")
                print(f"Group B: {ref_map[r2]}")
                print(f"Snippet A: {r1[:60]}...")
                print(f"Snippet B: {r2[:60]}...")

    if not found_dup_ref:
        print("No duplicate reflections found.")

if __name__ == "__main__":
    main()
