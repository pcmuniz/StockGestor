# Generated by Django 5.0.1 on 2024-04-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_gestor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fornecedores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_empresa", models.CharField(max_length=40)),
                ("cnpj", models.CharField(max_length=18)),
                ("inscricao_estadual", models.CharField(max_length=15)),
                ("inscricao_municipal", models.CharField(max_length=15)),
                ("endereco", models.CharField(default="NULL", max_length=40)),
                ("uf", models.CharField(default="NULL", max_length=2)),
                ("fornecedor_email", models.EmailField(max_length=40)),
                ("fornecedor_telefone", models.CharField(max_length=12)),
            ],
        ),
    ]
