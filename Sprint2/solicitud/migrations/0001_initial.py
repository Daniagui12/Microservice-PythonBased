# Generated by Django 3.2.6 on 2022-10-20 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('id_cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
    ]
