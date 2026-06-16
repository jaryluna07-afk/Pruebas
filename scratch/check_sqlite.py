import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Contacto, Usuario, Rol

print("=== ROLES ===")
for r in Rol.objects.all():
    print(f"ID: {r.id}, Nombre: {r.nombre_rol}")

print("\n=== USUARIOS ===")
for u in Usuario.objects.all():
    print(f"ID: {u.id}, Nombre: {u.nombre_usuario}, Email: {u.email}")

print("\n=== CONTACTOS ===")
print(f"Total contactos: {Contacto.objects.count()}")
for c in Contacto.objects.all():
    name = f"{c.nombre} {c.apellido}" if c.nombre else c.razon_social
    print(f"ID: {c.id}, Nombre: {name}, Doc/NIT: {c.documento_nit}, Teléfono: {c.telefono}, Celular: {c.celular}, Correo: {c.correo}")
