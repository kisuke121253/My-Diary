# Generated by Django 5.0.4 on 2024-05-06 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0013_remove_pagina_conteudo_pagina__conteudo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina',
            name='_conteudo',
        ),
    ]
