import json
import os

log_path = r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972\.system_generated\logs\transcript.jsonl"
out_path = r"c:\Users\Jary\OneDrive\Documentos\Pruebas\Pruebas\detalle_contacto_recovered.html"

print("Searching for write/replace tool calls of detalle_contacto.html in transcript.jsonl...")

best_content = None
max_len = 0

with open(log_path, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        try:
            data = json.loads(line)
            # check tool_calls
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                func = tc.get('function', {})
                name = func.get('name')
                args = func.get('arguments', {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception:
                        pass
                
                if not isinstance(args, dict):
                    continue
                    
                target = args.get('TargetFile', '')
                if 'detalle_contacto.html' in target:
                    content = args.get('CodeContent', '') or args.get('ReplacementContent', '')
                    if content and len(content) > max_len:
                        max_len = len(content)
                        best_content = content
                        print(f"Found match in line {line_num} with name {name}, size: {len(content)}")
        except Exception as e:
            # print(f"Error on line {line_num}: {e}")
            pass

if best_content:
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(best_content)
    print(f"Successfully recovered file to {out_path} with size {len(best_content)}")
else:
    print("No matching content found.")
