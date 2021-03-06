# Generated by Django 3.1.7 on 2021-04-20 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0002_auto_20210420_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='apellidoMaterno',
            new_name='apellido_materno',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='apellidoPaterno',
            new_name='apellido_paterno',
        ),
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('id_conexion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidentes.incidente')),
            ],
        ),
    ]
