from urllib import request
from django.shortcuts import redirect, render, HttpResponse
from .forms import RegistroForm
from .models import CustomUser, Fornecedores
from .models import Produtos
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

def home(request):
    return render(request, 'app_gestor/home.html')

# TDDO: criar login()
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/cadastro_produto")
        
    else:
        form = RegistroForm()
    
    return render(request, "app_gestor/registro.html", {"form":form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None
            print(user)
        if user is not None and check_password(password, user.password):
            return redirect('/cadastro_produto')
        else:
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'app_gestor/login.html', {'error_message': error_message})
    else:
        return render(request, 'app_gestor/login.html')

def logado(request):
    if request.method == "POST":
        form = request.POST
        fornecedor = Fornecedores(nome_empresa=form["nome_empresa"], cnpj=form["cnpj"], inscricao_estadual=form["ie"]
                                , inscricao_municipal=form["im"], endereco=form["endereco"], uf=form["uf"]
                                , fornecedor_email=form["email"], fornecedor_telefone=form["telefone"])
        fornecedor.save()
       
    return render(request, 'app_gestor/base_logado.html')

def cadastro_produto(request):
    if request.method == "POST":
        form = request.POST
        produto = Produtos(nome_produto=form["nome_produto"], ref=form["ref"], marca=form["marca"], categoria=form["categoria"], localizacao=form["localizacao"],
                            fornecedor=form["fornecedor"], data_entrada=form["data_entrada"], validade=form["validade"], codigo=form["codigo"],
                              codigo_barras=form["codigo_barras"], preco_compra=form["preco_compra"], descricao=form["descricao"])
        produto.save()

    return render(request, 'app_gestor/cadastro_produto.html')

def lista_produtos(request):
    produtos = Produtos.objects.all()

    return render(request, 'app_gestor/lista_produtos.html', {'produtos': produtos})

def lista_fornecedores(request):
    fornecedores = Fornecedores.objects.all()

    return render(request, 'app_gestor/lista_fornecedores.html', {'fornecedores': fornecedores})