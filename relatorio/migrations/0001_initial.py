# Generated by Django 4.2.1 on 2023-11-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('nome_usuario', models.CharField(max_length=100)),
                ('bloco_notas', models.TextField()),
            ],
        ),
    ]