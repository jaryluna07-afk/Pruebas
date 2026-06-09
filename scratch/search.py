import os
import json

log_path = r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972\.system_generated\logs\transcript.jsonl"

print("Checking if log file exists:", os.path.exists(log_path))
if not os.path.exists(log_path):
    # Try different case or parent directories
    print("Listing files in brain folder:")
    brain_dir = r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972"
    if os.path.exists(brain_dir):
        print(os.listdir(brain_dir))
        sys_gen = os.path.join(brain_dir, ".system_generated")
        if os.path.exists(sys_gen):
            print(".system_generated contents:", os.listdir(sys_gen))
            logs_dir = os.path.join(sys_gen, "logs")
            if os.path.exists(logs_dir):
                print("logs contents:", os.listdir(logs_dir))
else:
    # Search for premium-stats-card
    with open(log_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            if "premium-stats-card" in line or "Cumplimiento de Actividades" in line:
                print(f"Match found at line {idx + 1}")
                try:
                    data = json.loads(line)
                    # Print preview
                    content_str = data.get('content', '')
                    print("Source:", data.get('source'))
                    print("Type:", data.get('type'))
                    print("Length of content:", len(content_str))
                    # Let's save a chunk of content to a separate file so we can view it
                    out_path = f"c:\\Users\\Jary\\OneDrive\\Documentos\\Pruebas\\scratch\\match_{idx+1}.txt"
                    with open(out_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(content_str)
                    print("Saved to", out_path)
                except Exception as e:
                    print("Error parsing line:", e)
