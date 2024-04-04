from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login
from .forms import SignupForm
from .models import Fornecedores

def home(request):
    return render(request, 'app_gestor/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('base_logado')
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