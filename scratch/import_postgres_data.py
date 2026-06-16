import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import django

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from django.core.management import call_command

def main():
    db_engine = connection.settings_dict.get('ENGINE', '')
    print(f"Connecting to database with engine: {db_engine}")
    
    if 'sqlite' in db_engine:
        print("WARNING: You are currently connected to SQLite, not PostgreSQL!")
        print("Please set the DATABASE_URL environment variable to your Render PostgreSQL connection string.")
        print("Example (PowerShell): $env:DATABASE_URL='postgres://...'")
        print("Example (CMD): set DATABASE_URL=postgres://...")
        print("Example (Bash): export DATABASE_URL='postgres://...'")
        return
        
    export_file = os.path.join(os.path.dirname(__file__), 'local_data_export.json')
    if not os.path.exists(export_file):
        print(f"Error: Export file not found at {export_file}")
        print("Please run scratch/export_local_data.py first.")
        return

    print("Running migrations on PostgreSQL database to make sure tables exist...")
    call_command('migrate')

    print(f"Loading data from {export_file} into PostgreSQL...")
    try:
        call_command('loaddata', export_file)
        print("SUCCESS: Data successfully imported into Render PostgreSQL database!")
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Make sure your PostgreSQL database is clean and has no conflicting data.")

if __name__ == '__main__':
    main()
