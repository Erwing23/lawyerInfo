# Generated by Django 4.0.6 on 2022-08-03 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_alter_caso_fecha_fin_alter_caso_fecha_inicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='estadoSMS',
        ),
    ]