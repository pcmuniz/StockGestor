from django.shortcuts import redirect, render
from .forms import RegistroForm
from .models import CustomUser, Fornecedores, Produtos
from django.contrib.auth.hashers import check_password
from django.views import View

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'app_gestor/home.html')
    
class PaginaServicosView(View):
    def get(self, request):
        return render(request, 'app_gestor/servicos.html')
    
class PaginaSobreView(View):
    def get(self, request):
        return render(request, 'app_gestor/sobre.html')
    
class PaginaContatoView(View):
    def get(self, request):
        return render(request, 'app_gestor/contato.html')

class RegistroView(View):
    # TDDO: criar login()
    def get(self, request):
        form = RegistroForm()
        return render(request, 'app_gestor/registro.html', {'form': form})
    
    def post(self, request):
        if request.method == "POST":
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/login")
            
        else:
            form = RegistroForm()
        
        return render(request, "app_gestor/registro.html", {"form":form})

class LoginView(View):
    def get(self, request):
        return render(request, 'app_gestor/login.html')
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                user = None
                print(user)
            if user is not None and check_password(password, user.password):
                return redirect('/lista_produtos')
            else:
                error_message = "Credenciais inválidas. Por favor, tente novamente."
                return render(request, 'app_gestor/login.html', {'error_message': error_message})
        else:
            return render(request, 'app_gestor/login.html')

class ListaProdutosView(View):
    def get(self, request):
        produtos = Produtos.objects.all()

        return render(request, 'app_gestor/lista_produtos.html', {'produtos': produtos})

class CadastroProdutosView(View):
    def get(self, request):
        return render(request, 'app_gestor/cadastro_produto.html')
    
    def post(self, request):
        if request.method == "POST":
            form = request.POST
            produto = Produtos(nome_produto=form["nome_produto"], ref=form["ref"], marca=form["marca"], categoria=form["categoria"], localizacao=form["localizacao"],
                                fornecedor=form["fornecedor"], data_entrada=form["data_entrada"], validade=form["validade"], codigo=form["codigo"],
                                quantidade=form["quantidade"], codigo_barras=form["codigo_barras"], preco_compra=form["preco_compra"], descricao=form["descricao"])
            produto.save()

        return render(request, 'app_gestor/cadastro_produto.html')

class ListaFornecedoresView(View):
    def get(self, request):
        fornecedores = Fornecedores.objects.all()
        return render(request, 'app_gestor/lista_fornecedores.html', {'fornecedores': fornecedores})

class CadastroFornecedorView(View):
    def get(self, request):
        return render(request, 'app_gestor/cadastro_fornecedor.html')

    def post(self, request):
        if request.method == "POST":
            form = request.POST
            fornecedor = Fornecedores(nome_empresa=form["nome_empresa"], cnpj=form["cnpj"], inscricao_estadual=form["ie"]
                                    , inscricao_municipal=form["im"], endereco=form["endereco"], uf=form["uf"]
                                    , fornecedor_email=form["email"], fornecedor_telefone=form["telefone"])
            fornecedor.save()
        
        return render(request, 'app_gestor/cadastro_fornecedor.html')





