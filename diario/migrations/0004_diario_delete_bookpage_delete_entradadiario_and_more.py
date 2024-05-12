# Generated by Django 5.0.3 on 2024-04-10 05:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0003_bookpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='BookPage',
        ),
        migrations.DeleteModel(
            name='EntradaDiario',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
