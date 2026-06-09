# Generated manually

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_firmadigital'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaccion',
            name='canal_comunicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interacciones_canal', to='core.tipointeraccion'),
        ),
        migrations.AddField(
            model_name='interaccion',
            name='duracion_minutos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interaccion',
            name='temperatura_emocional',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]
