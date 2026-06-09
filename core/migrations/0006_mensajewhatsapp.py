# Generated manually

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_interaction_analytics_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeWhatsApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('direccion', models.CharField(choices=[('Entrante', 'Entrante'), ('Saliente', 'Saliente')], max_length=10)),
                ('whatsapp_id', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(default='enviado', max_length=20)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_whatsapp', to='core.contacto')),
                ('remitente_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.usuario')),
            ],
        ),
    ]
