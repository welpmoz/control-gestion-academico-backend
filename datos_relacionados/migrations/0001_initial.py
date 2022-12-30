# Generated by Django 4.1.4 on 2022-12-30 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_simples', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('datos_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_simples.carrera')),
                ('datos_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_simples.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditos', models.IntegerField()),
                ('tipo', models.CharField(max_length=1)),
                ('grupo', models.CharField(max_length=1)),
                ('ht', models.TimeField()),
                ('hp', models.TimeField()),
                ('dia', models.CharField(max_length=15)),
                ('hi', models.TimeField()),
                ('hf', models.TimeField()),
                ('aula', models.CharField(max_length=20)),
                ('curso_activo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_relacionados.cursoactivo')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
