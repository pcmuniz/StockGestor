# Generated by Django 5.0.1 on 2024-05-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestor', '0006_produtos_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(default=1),
        ),
    ]
