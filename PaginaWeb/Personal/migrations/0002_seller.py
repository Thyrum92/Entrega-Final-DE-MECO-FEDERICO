# Generated by Django 4.2.5 on 2023-09-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('nickname', models.CharField(max_length=25)),
                ('razon_social', models.CharField(max_length=25)),
                ('nombre_responsable', models.CharField(max_length=20)),
                ('apellido_responsable', models.CharField(max_length=20)),
                ('cotacto_resonsable', models.EmailField(max_length=30)),
                ('servicio_0', models.CharField(max_length=15)),
                ('servicio_1', models.CharField(max_length=15)),
                ('servicio_2', models.CharField(max_length=15)),
                ('servicio_3', models.CharField(max_length=15)),
                ('servicio_4', models.CharField(max_length=15)),
            ],
        ),
    ]
