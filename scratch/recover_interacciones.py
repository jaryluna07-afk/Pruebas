import json
import os

logs_to_search = [
    r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972\.system_generated\logs\transcript.jsonl",
    r"C:\Users\Jary\.gemini\antigravity\brain\d2a03672-c636-4013-b167-e43459e4dfc7\.system_generated\logs\transcript.jsonl"
]

out_dir = r"c:\Users\Jary\OneDrive\Documentos\Pruebas\scratch"
os.makedirs(out_dir, exist_ok=True)

print("Starting recovery search...")
version_count = 0

for log_path in logs_to_search:
    if not os.path.exists(log_path):
        print(f"Log path does not exist: {log_path}")
        continue
    print(f"Searching in {log_path}...")
    with open(log_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                # Check tool calls
                tool_calls = data.get('tool_calls', [])
                for tc in tool_calls:
                    func = tc.get('function', {})
                    args = func.get('arguments', {})
                    if isinstance(args, str):
                        try:
                            args = json.loads(args)
                        except:
                            pass
                    if not isinstance(args, dict):
                        continue
                    
                    target = args.get('TargetFile', '') or args.get('Target', '') or args.get('AbsolutePath', '')
                    if 'interacciones.html' in target:
                        content = args.get('CodeContent', '') or args.get('ReplacementContent', '')
                        if content:
                            version_count += 1
                            out_file = os.path.join(out_dir, f"interacciones_v{version_count}.html")
                            with open(out_file, 'w', encoding='utf-8') as out_f:
                                out_f.write(content)
                            print(f"Found version {version_count} (length {len(content)}) at line {line_num}. Wrote to {out_file}")
            except Exception as e:
                pass

print(f"Finished. Found {version_count} versions.")
