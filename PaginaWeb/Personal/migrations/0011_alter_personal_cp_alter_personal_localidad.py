# Generated by Django 4.2.5 on 2023-09-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0010_alter_personal_direccion_alter_personal_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cp',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='personal',
            name='localidad',
            field=models.CharField(default='a', max_length=15),
        ),
    ]
