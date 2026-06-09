import os
import django
from django.db.models import Q, Avg, Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Interaccion, TipoInteraccion

print("Total Interacciones:", Interaccion.objects.count())

# Let's see some details
for inter in Interaccion.objects.all().order_by('-fecha_interaccion')[:15]:
    channel = 'None'
    if inter.canal_comunicacion:
        channel = inter.canal_comunicacion.nombre_tipo
    elif inter.tipo_interaccion:
        channel = inter.tipo_interaccion.nombre_tipo
    print(f"ID: {inter.id}, Date: {inter.fecha_interaccion}, Reunion Date: {inter.fecha_reunion}, Duration: {inter.duracion_minutos}, Channel: {channel}, Estado: {inter.estado}")

print("\n--- Detailed Count by Month/Year and Channel ---")
for year in [2026]:
    for month in range(1, 13):
        # By fecha_interaccion
        qs_fi = Interaccion.objects.filter(fecha_interaccion__year=year, fecha_interaccion__month=month)
        calls_fi = qs_fi.filter(Q(canal_comunicacion__nombre_tipo='Llamada') | Q(tipo_interaccion__nombre_tipo='Llamada')).count()
        meetings_fi = qs_fi.filter(Q(canal_comunicacion__nombre_tipo='Reunión') | Q(tipo_interaccion__nombre_tipo='Reunión')).count()
        emails_fi = qs_fi.filter(Q(canal_comunicacion__nombre_tipo='Correo') | Q(tipo_interaccion__nombre_tipo='Correo')).count()
        
        # By fecha_reunion for Calls/Meetings, and fecha_interaccion for Correos
        # Let's count them
        calls_fr = Interaccion.objects.filter(
            Q(canal_comunicacion__nombre_tipo='Llamada') | Q(tipo_interaccion__nombre_tipo='Llamada')
        ).filter(
            Q(fecha_reunion__year=year, fecha_reunion__month=month) |
            Q(fecha_reunion__isnull=True, fecha_interaccion__year=year, fecha_interaccion__month=month)
        ).count()
        
        meetings_fr = Interaccion.objects.filter(
            Q(canal_comunicacion__nombre_tipo='Reunión') | Q(tipo_interaccion__nombre_tipo='Reunión')
        ).filter(
            Q(fecha_reunion__year=year, fecha_reunion__month=month) |
            Q(fecha_reunion__isnull=True, fecha_interaccion__year=year, fecha_interaccion__month=month)
        ).count()
        
        emails_fr = Interaccion.objects.filter(
            Q(canal_comunicacion__nombre_tipo='Correo') | Q(tipo_interaccion__nombre_tipo='Correo')
        ).filter(
            fecha_interaccion__year=year, fecha_interaccion__month=month
        ).count()
        
        if max(calls_fi, meetings_fi, emails_fi, calls_fr, meetings_fr, emails_fr) > 0:
            print(f"{year}-{month:02d}:")
            print(f"  By fecha_interaccion: Calls={calls_fi}, Meetings={meetings_fi}, Emails={emails_fi}")
            print(f"  By hybrid/reunion: Calls={calls_fr}, Meetings={meetings_fr}, Emails={emails_fr}")
