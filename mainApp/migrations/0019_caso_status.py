# Generated by Django 4.0.6 on 2022-08-06 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0018_alter_aprobaciones_status_alter_contacto_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='status',
            field=models.CharField(choices=[('ACT', 'ACTIVO'), ('CERR', 'INACTIVO')], default='ACT', max_length=5),
        ),
    ]
