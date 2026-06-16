# Generated manually to ensure safe data conversion in SQLite/Postgres
from django.db import migrations, models
import django.db.models.deletion

def populate_defaults_and_migrate_data(apps, schema_editor):
    TipoProyecto = apps.get_model('core', 'TipoProyecto')
    Proyecto = apps.get_model('core', 'Proyecto')
    Contacto = apps.get_model('core', 'Contacto')

    # 1. Create default Project Types
    types_list = [
        "Construcción desde cero en terreno propio",
        "Diseño y construcción de casas personalizadas",
        "Trámites legales y licencias",
        "Adecuaciones o remodelaciones",
        "Apartamento"
    ]
    type_objs = {}
    for name in types_list:
        obj, _ = TipoProyecto.objects.get_or_create(nombre_tipo=name)
        type_objs[name] = obj

    # 2. Create default Projects (all under "Apartamento")
    apartamento_type = type_objs["Apartamento"]
    projects_list = [
        "Satori (Ibagué)",
        "Mandala (Ibagué)",
        "Selvia (Armenia)",
        "Ícono 60 (Ibagué)",
        "Ática (Ibagué)",
        "Vivalto (Ibagué)",
        "Morada Pinaos (Ibagué)"
    ]
    project_objs = {}
    for name in projects_list:
        obj, _ = Proyecto.objects.get_or_create(tipo_proyecto=apartamento_type, nombre_proyecto=name)
        project_objs[name] = obj

    # 3. Migrate data in Contacto from old text columns to new ForeignKey columns
    for c in Contacto.objects.all():
        old_tp = c.tipo_proyecto_old
        old_pn = c.proyecto_nombre_old

        tp_obj = None
        pn_obj = None

        if old_tp:
            # Clean and look up project type
            tp_obj = TipoProyecto.objects.filter(nombre_tipo=old_tp).first()
            # If not found in defaults, create it dynamically
            if not tp_obj:
                tp_obj = TipoProyecto.objects.create(nombre_tipo=old_tp)

        if old_pn:
            # Clean and look up project
            # If we have a project type, we relate it, otherwise fallback to Apartamento
            parent_type = tp_obj if tp_obj else apartamento_type
            pn_obj = Proyecto.objects.filter(nombre_proyecto=old_pn, tipo_proyecto=parent_type).first()
            if not pn_obj:
                pn_obj = Proyecto.objects.create(nombre_proyecto=old_pn, tipo_proyecto=parent_type)

        c.tipo_proyecto = tp_obj
        c.proyecto_nombre = pn_obj
        c.save(update_fields=['tipo_proyecto', 'proyecto_nombre'])

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contacto_apartamento_contacto_edad_and_more'),
    ]

    operations = [
        # Create models TipoProyecto and Proyecto
        migrations.CreateModel(
            name='TipoProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=150, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('tipo_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='core.tipoproyecto')),
            ],
        ),
        # Rename existing CharFields to _old
        migrations.RenameField(
            model_name='contacto',
            old_name='tipo_proyecto',
            new_name='tipo_proyecto_old',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='proyecto_nombre',
            new_name='proyecto_nombre_old',
        ),
        # Add new ForeignKey fields
        migrations.AddField(
            model_name='contacto',
            name='tipo_proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tipoproyecto'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='proyecto_nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.proyecto'),
        ),
        # Run python script to migrate data
        migrations.RunPython(populate_defaults_and_migrate_data),
        # Remove old _old fields
        migrations.RemoveField(
            model_name='contacto',
            name='tipo_proyecto_old',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='proyecto_nombre_old',
        ),
    ]
