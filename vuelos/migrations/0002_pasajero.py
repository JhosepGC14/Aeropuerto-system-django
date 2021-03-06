# Generated by Django 3.0.5 on 2020-04-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('vuelo', models.ManyToManyField(blank=True, related_name='pasajeros', to='vuelos.Vuelo')),
            ],
        ),
    ]
