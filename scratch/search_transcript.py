import json

log_path = r"C:\Users\Jary\.gemini\antigravity\brain\c0ea56e9-ad9f-41f4-94d4-b6dd86c78972\.system_generated\logs\transcript.jsonl"

print("Searching transcript for modifications to views.py or interacciones.html...")

with open(log_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        try:
            data = json.loads(line)
            source = data.get('source', '')
            t = data.get('type', '')
            tool_calls = data.get('tool_calls', [])
            
            for tc in tool_calls:
                name = tc.get('name')
                args = tc.get('args', {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except:
                        pass
                if not isinstance(args, dict):
                    continue
                
                target = args.get('TargetFile', '') or args.get('AbsolutePath', '')
                if 'views.py' in target or 'interacciones.html' in target:
                    print(f"Step {data.get('step_index')}: {name} on {target}")
                    desc = args.get('Description', '') or args.get('Instruction', '')
                    if desc:
                        print(f"  Description/Instruction: {desc}")
        except Exception as e:
            pass
