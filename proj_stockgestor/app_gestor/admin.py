from django.contrib import admin
from .models import Produtos, Fornecedores
# Register your models here.

admin.site.register(Produtos)
admin.site.register(Fornecedores)