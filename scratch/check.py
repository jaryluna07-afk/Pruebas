import os
import sqlite3

# 1. Read the last 20 lines of error.txt (handling UTF-16LE)
error_path = r"c:\Users\Jary\OneDrive\Documentos\Pruebas\error.txt"
if os.path.exists(error_path):
    print("--- LAST 20 LINES OF ERROR.TXT ---")
    try:
        with open(error_path, "r", encoding="utf-16le") as f:
            lines = f.readlines()
            for line in lines[-20:]:
                print(line.strip())
    except Exception as e:
        print("Error reading error.txt:", e)
else:
    print("error.txt not found")

# 2. Check the database for saved attachment URLs
db_path = r"c:\Users\Jary\OneDrive\Documentos\Pruebas\db.sqlite3"
if os.path.exists(db_path):
    print("\n--- ATTACHMENT ENTRIES IN DB ---")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, detalle_actividad FROM core_interaccion WHERE detalle_actividad LIKE '%adjuntos_correo%' LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}")
            # print part containing adjuntos_correo
            idx = row[1].find("adjuntos_correo")
            start = max(0, idx - 100)
            end = min(len(row[1]), idx + 200)
            print("...", row[1][start:end], "...")
        conn.close()
    except Exception as e:
        print("Error reading database:", e)
else:
    print("db.sqlite3 not found")
