import os
import django
from django.db.models import Q, Avg, Sum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Interaccion, Contacto

print("--- Dump of Averages for all contacts and months ---")
for contacto in Contacto.objects.all():
    print(f"\nContacto: {contacto.nombre} {contacto.apellido} (ID: {contacto.id})")
    
    # Let's find all unique months for this contact's interactions
    dates = Interaccion.objects.filter(contacto=contacto).values_list('fecha_reunion', 'fecha_interaccion')
    months = set()
    for fr, fi in dates:
        if fr:
            months.add((fr.year, fr.month))
        if fi:
            months.add((fi.year, fi.month))
            
    for year, month in sorted(months):
        q_event = (
            (Q(canal_comunicacion__nombre_tipo__in=['Llamada', 'Reunión']) | Q(tipo_interaccion__nombre_tipo__in=['Llamada', 'Reunión'])) &
            (Q(fecha_reunion__year=year, fecha_reunion__month=month) | Q(fecha_reunion__isnull=True, fecha_interaccion__year=year, fecha_interaccion__month=month))
        )
        q_other = (
            ~Q(tipo_interaccion__nombre_tipo__in=['Llamada', 'Reunión']) & 
            (Q(canal_comunicacion__isnull=True) | ~Q(canal_comunicacion__nombre_tipo__in=['Llamada', 'Reunión'])) &
            Q(fecha_interaccion__year=year, fecha_interaccion__month=month)
        )
        
        inters = Interaccion.objects.filter(contacto=contacto).filter(q_event | q_other)
        calls = inters.filter(Q(canal_comunicacion__nombre_tipo='Llamada') | Q(tipo_interaccion__nombre_tipo='Llamada'))
        meetings = inters.filter(Q(canal_comunicacion__nombre_tipo='Reunión') | Q(tipo_interaccion__nombre_tipo='Reunión'))
        
        calls_timed = calls.filter(duracion_minutos__gt=0)
        meetings_timed = meetings.filter(duracion_minutos__gt=0)
        
        avg_call = calls_timed.aggregate(avg=Avg('duracion_minutos'))['avg'] or 0
        avg_meeting = meetings_timed.aggregate(avg=Avg('duracion_minutos'))['avg'] or 0
        
        timed_count = calls_timed.count() + meetings_timed.count()
        total_dur = (calls_timed.aggregate(total=Sum('duracion_minutos'))['total'] or 0) + (meetings_timed.aggregate(total=Sum('duracion_minutos'))['total'] or 0)
        weighted_avg = total_dur / timed_count if timed_count > 0 else 0
        
        # Calculate possible formulas:
        # 1. Simple average of category averages (if both exist, else the non-zero one)
        if avg_call > 0 and avg_meeting > 0:
            simple_avg = (avg_call + avg_meeting) / 2
        else:
            simple_avg = avg_call if avg_call > 0 else avg_meeting
            
        print(f"  {year}-{month:02d}:")
        print(f"    Calls: count={calls.count()}, timed={calls_timed.count()}, avg={avg_call:.2f}")
        print(f"    Meetings: count={meetings.count()}, timed={meetings_timed.count()}, avg={avg_meeting:.2f}")
        print(f"    Weighted Avg (overall_avg_min): {weighted_avg:.2f}")
        print(f"    Simple Avg of Averages: {simple_avg:.2f}")
