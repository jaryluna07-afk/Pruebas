import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(core_interaccion);")
columns = cursor.fetchall()
for col in columns:
    print(col)
conn.close()
