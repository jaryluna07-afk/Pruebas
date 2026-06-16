import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import psycopg2

def main():
    print("Checking local PostgreSQL database 'db_dyco'...")
    try:
        conn = psycopg2.connect(
            dbname="db_dyco",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM core_contacto;")
        count = cur.fetchone()[0]
        print(f"Connection successful! Total contacts in local PostgreSQL: {count}")
        
        cur.execute("SELECT id, nombre, apellido, razon_social, documento_nit, correo FROM core_contacto;")
        rows = cur.fetchall()
        for r in rows:
            name = f"{r[1]} {r[2]}" if r[1] else r[3]
            print(f"ID: {r[0]}, Nombre: {name}, Doc: {r[4]}, Correo: {r[5]}")
            
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Could not connect to local PostgreSQL 'db_dyco': {e}")

if __name__ == '__main__':
    main()
