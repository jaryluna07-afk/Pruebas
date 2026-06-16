import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import django
from django.core import serializers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Rol, Usuario, TipoIdentificacion, TipoContacto, TipoInteraccion, TipoProyecto, Proyecto, Contacto, Interaccion, Compromiso, FirmaDigital, MensajeWhatsApp

# List of models we want to export in order of dependency
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

exported_data = []

print("Exporting data from SQLite...")
for model in models_to_export:
    queryset = model.objects.all()
    count = queryset.count()
    print(f"Model {model.__name__}: {count} records found.")
    if count > 0:
        # Serialize to python objects first to accumulate them
        data_serialized = serializers.serialize('python', queryset)
        exported_data.extend(data_serialized)

# Write to file
export_path = os.path.join(os.path.dirname(__file__), 'local_data_export.json')
with open(export_path, 'w', encoding='utf-8') as f:
    # We serialize the accumulated list back to JSON
    # To do this, we can use django's serializer directly on the django objects,
    # but since we want them in a single array in order, let's serialize them all at once.
    # We need a list of all objects.
    all_objects = []
    for model in models_to_export:
        all_objects.extend(list(model.objects.all()))
    
    serializers.serialize('json', all_objects, indent=4, stream=f)

print(f"Data successfully exported to {export_path}")
