# Generated by Django 3.0.5 on 2020-04-12 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areopuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.IntegerField(null=True)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='llegadas', to='vuelos.Areopuerto')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salida', to='vuelos.Areopuerto')),
            ],
        ),
    ]