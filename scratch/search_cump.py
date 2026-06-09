import os

root_dir = r"c:\Users\Jary\OneDrive\Documentos\Pruebas"
search_terms = ["cumplimiento", "stats_json", "act_total"]

print("Scanning workspace files...")
for root, dirs, files in os.walk(root_dir):
    if ".git" in dirs:
        dirs.remove(".git")
    if "env" in dirs:
        dirs.remove("env")
    if "__pycache__" in dirs:
        dirs.remove("__pycache__")
        
    for file in files:
        if file.endswith((".html", ".py", ".css", ".js", ".txt")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    found = [term for term in search_terms if term.lower() in content.lower()]
                    if found:
                        print(f"File: {path} contains: {found}")
            except Exception as e:
                pass
print("Scan complete.")
