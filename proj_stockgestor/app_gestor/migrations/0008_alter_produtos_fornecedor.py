# Generated by Django 5.0.1 on 2024-05-12 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestor', '0007_alter_produtos_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestor.fornecedores'),
        ),
    ]
