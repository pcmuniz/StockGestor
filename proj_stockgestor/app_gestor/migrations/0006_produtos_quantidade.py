# Generated by Django 5.0.3 on 2024-04-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestor', '0005_alter_produtos_codigo_alter_produtos_codigo_barras'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]