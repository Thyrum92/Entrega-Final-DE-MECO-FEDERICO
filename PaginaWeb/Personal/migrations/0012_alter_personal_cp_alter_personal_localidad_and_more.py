# Generated by Django 4.2.5 on 2023-09-23 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0011_alter_personal_cp_alter_personal_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal',
            name='localidad',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='personal',
            name='nombre_emergencia',
            field=models.CharField(default='a', max_length=60),
        ),
        migrations.AlterField(
            model_name='personal',
            name='numero_contacto',
            field=models.IntegerField(default=1),
        ),
    ]
