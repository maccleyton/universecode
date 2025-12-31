import os
import re

jornada_dir = r"e:\Desenvolvimento\universecode\literatura\jornada"
files = os.listdir(jornada_dir)

print("Renomeando arquivos em jornada...")
for filename in files:
    # Match "Capítulo XX.png" or "Capítulo XX.md"
    match = re.match(r"Capítulo (\d+)\.(png|md|jpg|jpeg)", filename, re.IGNORECASE)
    if match:
        num = match.group(1)
        ext = match.group(2)
        new_name = f"cap_{num}.{ext}"
        old_path = os.path.join(jornada_dir, filename)
        new_path = os.path.join(jornada_dir, new_name)
        
        # Avoid overwriting if exists (though unlikely here unless duplicates)
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        else:
            print(f"Skipped {filename}, {new_name} already exists.")

print("Concluído.")
