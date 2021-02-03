# Generated by Django 3.1.5 on 2021-02-01 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]