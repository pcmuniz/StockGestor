# Generated by Django 5.0.3 on 2024-04-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestor', '0003_produtos'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(default='Descrição', max_length=100),
        ),
    ]
