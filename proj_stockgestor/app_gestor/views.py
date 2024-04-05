from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login
from .forms import SignupForm
from .models import Fornecedores
from .models import Produtos

def home(request):
    return render(request, 'app_gestor/home.html')

# TDDO: criar login()
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('app_gestor/base_logado.html')
    else:
        form = SignupForm()
    return render(request,'app_gestor/registro.html',{'form': form})


def logado(request):
    if request.method == "POST":
        form = request.POST
        fornecedor = Fornecedores(nome_empresa=form["nome_empresa"], cnpj=form["cnpj"], inscricao_estadual=form["ie"]\
                                , inscricao_municipal=form["im"], endereco=form["endereco"], uf=form["uf"]\
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
