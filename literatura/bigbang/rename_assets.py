
import os
import shutil

ASSETS_DIR = r"e:\Desenvolvimento\universecode\literatura\bigbang\assets"

def rename_assets():
    if not os.path.exists(ASSETS_DIR):
        print(f"Directory not found: {ASSETS_DIR}")
        return

    print(f"Scanning {ASSETS_DIR}...")
    
    for filename in os.listdir(ASSETS_DIR):
        # Rename CXX.jpeg to cap_XX.jpg
        if filename.startswith("C") and (filename.endswith(".jpeg") or filename.endswith(".jpg")):
            # Extract number
            name_part = filename.split('.')[0] # C01
            try:
                num = int(name_part[1:])
                new_name = f"cap_{num:02d}.jpg"
                old_path = os.path.join(ASSETS_DIR, filename)
                new_path = os.path.join(ASSETS_DIR, new_name)
                
                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {filename} -> {new_name}")
            except ValueError:
                print(f"Skipping {filename}, number parse error")
        
        # Rename AXX.png/E01 to part_XX ?? 
        # User said: "assets/part_X.jpg". I only have A01, A02.
        # I will leave Axx for now or maybe rename A01 to part_01? 
        # Without knowing mapping for sure, I'll stick to chapters which are obvious.

if __name__ == "__main__":
    rename_assets()
