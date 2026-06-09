import json
import os

log_path = r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972\.system_generated\logs\transcript.jsonl"
out_path = r"c:\Users\Jary\OneDrive\Documentos\Pruebas\scratch\recovered_premium.html"

print("Scanning log file...")
found_content = None

with open(log_path, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        try:
            data = json.loads(line)
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                func = tc.get('function', {})
                args = func.get('arguments', {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except Exception:
                        pass
                if not isinstance(args, dict):
                    continue
                
                # Check if this tool call wrote or replaced file content for detalle_contacto.html
                target = args.get('TargetFile', '')
                if 'detalle_contacto.html' in target:
                    content = args.get('CodeContent', '') or args.get('ReplacementContent', '')
                    if content and 'stats_json' in content:
                        found_content = content
                        print(f"Found match on line {line_num}! Size: {len(content)}")
        except Exception as e:
            pass

if found_content:
    with open(out_path, 'w', encoding='utf-8') as f_out:
        f_out.write(found_content)
    print(f"Success! Saved recovered premium template to {out_path}")
else:
    print("No matching content containing 'stats_json' was found in the logs.")
