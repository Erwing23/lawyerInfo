# Generated by Django 4.0.6 on 2022-09-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0021_remove_aprobaciones_user_remove_caso_aprobaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprobaciones',
            name='status',
            field=models.CharField(choices=[('ABI', 'ABIERTO'), ('CERR', 'CERRADO')], default='ABI', max_length=5),
        ),
        migrations.AlterField(
            model_name='caso',
            name='status',
            field=models.CharField(choices=[('ACT', 'ACTIVO'), ('CERR', 'CERRADO'), ('INACT', 'INACTIVO')], default='ACT', max_length=5),
        ),
    ]
