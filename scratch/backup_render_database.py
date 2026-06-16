import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import django
from django.core import serializers

# Ensure settings module is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection
from core.models import Rol, Usuario, TipoIdentificacion, TipoContacto, TipoInteraccion, TipoProyecto, Proyecto, Contacto, Interaccion, Compromiso, FirmaDigital, MensajeWhatsApp

def main():
    db_engine = connection.settings_dict.get('ENGINE', '')
    db_name = connection.settings_dict.get('NAME', '')
    print(f"Connecting to database: {db_name} ({db_engine})")
    
    if 'sqlite' in db_engine:
        print("WARNING: You are currently connected to the local SQLite database.")
        print("To backup the Render database, you must set the DATABASE_URL environment variable first.")
        print("Example (PowerShell): $env:DATABASE_URL='postgres://...'")
        return

    models_to_export = [
        Rol,
        Usuario,
        TipoIdentificacion,
        TipoContacto,
        TipoInteraccion,
        TipoProyecto,
        Proyecto,
        Contacto,
        Interaccion,
        Compromiso,
        FirmaDigital,
        MensajeWhatsApp
    ]

    all_objects = []
    print("Exporting data from Render PostgreSQL...")
    for model in models_to_export:
        queryset = model.objects.all()
        count = queryset.count()
        print(f"Model {model.__name__}: {count} records found.")
        all_objects.extend(list(queryset))

    backup_path = os.path.join(os.path.dirname(__file__), 'render_data_backup.json')
    with open(backup_path, 'w', encoding='utf-8') as f:
        serializers.serialize('json', all_objects, indent=4, stream=f)

    print(f"SUCCESS: Render database successfully backed up to {backup_path}!")

if __name__ == '__main__':
    main()
