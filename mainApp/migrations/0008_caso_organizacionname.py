# Generated by Django 4.0.6 on 2022-08-02 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_remove_caso_organizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='organizacionName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.organizacion'),
        ),
    ]