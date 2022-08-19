# Generated by Django 4.0.6 on 2022-08-19 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_alter_caso_fecha_fin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aprobaciones',
            name='User',
        ),
        migrations.RemoveField(
            model_name='caso',
            name='aprobaciones',
        ),
        migrations.AddField(
            model_name='aprobaciones',
            name='caso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.caso'),
        ),
    ]
