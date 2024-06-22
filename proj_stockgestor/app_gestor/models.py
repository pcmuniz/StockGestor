from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date
from django.utils import timezone


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('grupos'),
        blank=True,
        help_text=(
            'Os grupos aos quais este usuário pertence. Um usuário terá todas as permissões '
            'concedidas a cada um de seus grupos.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('permissões do usuário'),
        blank=True,
        help_text=('Permissões específicas para este usuário.'),
        related_name="custom_user_set",  
        related_query_name="user",
    )

    def __str__(self) -> str:
        return self.username
    

class Fornecedores(models.Model):
    nome_empresa = models.CharField(max_length = 40)
    cnpj = models.CharField(max_length = 18)
    inscricao_estadual = models.CharField(max_length = 15)
    inscricao_municipal = models.CharField(max_length = 15)
    endereco = models.CharField(max_length = 40, default="NULL")
    uf = models.CharField(max_length = 2, default="NULL")
    fornecedor_email = models.EmailField(max_length = 40)
    fornecedor_telefone = models.CharField(max_length = 12)

    def __str__(self):
        return self.nome_empresa

class Produtos(models.Model):
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    quantidade = models.IntegerField(default=1)
    quantidade_alerta = models.IntegerField(default=1)
    codigo_barras = models.IntegerField()
    preco_compra = models.FloatField(max_length=8)
    nome_produto = models.CharField(max_length=40)
    ref = models.CharField(max_length=30)
    marca = models.CharField(max_length=15)
    categoria = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=3)
    descricao = models.CharField(max_length=100, default="Descrição")
    data_entrada = models.DateField()
    validade = models.DateField()

    def __str__(self):
        return "[" + str(self.id) + "] " + self.nome_produto
    
    # def vencimento(self):
    #     hoje = date.today()
    #     return(self.validade - self.data_entrada).days

    def vencimento(self):
        diferenca = self.validade - self.data_entrada
        dias_diferenca = diferenca.days
        return dias_diferenca


    @property
    def preco_total(self):
        return self.preco_compra * self.quantidade