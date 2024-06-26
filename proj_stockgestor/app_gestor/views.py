from urllib import request
from django.shortcuts import get_object_or_404, redirect, render # type: ignore
from .forms import RegistroForm
from .models import CustomUser, Fornecedores, Produtos
from django.contrib.auth.hashers import check_password # type: ignore
from django.contrib import messages # type: ignore
from django.views import View
from django.db.models import F, FloatField, ExpressionWrapper, Sum
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone

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

class PaginaEditarProduto(View):
    def get(self, request):
        return render(request, 'app_gestor/editar_produto.html')
    
class ValorEstoqueView(View):
    def get(self, request):
        return render(request, 'app_gestor/valor_estoque.html')
    
class AlertaVencimento(View):
    def get(self, request):
        produtos = Produtos.objects.all()
        return render(request, 'app_gestor/lista_produtos.html', {'produtos' : produtos})
    
class ValorEstoqueView(View):
    def get(self, request):
        produtos = Produtos.objects.all()

        valor_total = ExpressionWrapper(
            F('preco_compra') * F('quantidade'),
            output_field=FloatField()
        )

        soma_valor_estoque = produtos.aggregate(total=Sum(valor_total))

        context = {
            'produtos': produtos,
            'soma_valor_estoque': soma_valor_estoque['total'],
        }

        return render(request, 'app_gestor/valor_estoque.html', context)



class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'app_gestor/registro.html', {'form': form})
    
    def post(self, request):
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None
            print(user)
        if user is not None and check_password(password, user.password):
            return redirect('/produtos')
        else:
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'app_gestor/login.html', {'error_message': error_message})

class ListaProdutosView(View):
    def get(self, request):
        produtos = Produtos.objects.all()
        fornecedores = Fornecedores.objects.all()
        filtro = False
        return render(request, 'app_gestor/lista_produtos.html', {'produtos': produtos,'fornecedores': fornecedores, 'filtro': filtro})
    

    def post(self, request):
        produtos = Produtos.objects.all()
        fornecedores = Fornecedores.objects.all()
        try:
            fornecedor_escolhido = request.POST["fornecedor_escolhido"]
        except:
            raise MultiValueDictKeyError("Escolha outra opção!")
            
        return render(request, 'app_gestor/lista_produtos.html',{'produtos': produtos, 'fornecedores': fornecedores, 'fornecedor_filtro': fornecedor_escolhido})
        

class CadastroProdutosView(View):
    def get(self, request):
        fornecedores = Fornecedores.objects.all()
        return render(request, 'app_gestor/cadastro_produto.html', {'fornecedores': fornecedores})
    
    def post(self, request): 
        fornecedores = Fornecedores.objects.all()
        form = request.POST
        fornecedor_cadastrado = Fornecedores.objects.get(nome_empresa = form["fornecedor"])
        produto = Produtos(nome_produto=form["nome_produto"], ref=form["ref"], marca=form["marca"], categoria=form["categoria"], localizacao=form["localizacao"],
                            fornecedor=fornecedor_cadastrado, data_entrada=timezone.now(), validade=form["validade"], codigo=form["codigo"],
                            quantidade=form["quantidade"], quantidade_alerta=form["quantidade_alerta"], codigo_barras=form["codigo_barras"], preco_compra=form["preco_compra"], descricao=form["descricao"])
        produto.save()
        messages.info(request, 'Produto cadastrado com sucesso.')

        return render(request, 'app_gestor/cadastro_produto.html', {'fornecedores': fornecedores})

class ListaFornecedoresView(View):
    def get(self, request):
        fornecedores = Fornecedores.objects.all()
        return render(request, 'app_gestor/lista_fornecedores.html', {'fornecedores': fornecedores})

class CadastroFornecedorView(View):
    def get(self, request):
        return render(request, 'app_gestor/cadastro_fornecedor.html')

    def post(self, request):
        form = request.POST
        fornecedor = Fornecedores(nome_empresa=form["nome_empresa"], cnpj=form["cnpj"], inscricao_estadual=form["ie"]
                                , inscricao_municipal=form["im"], endereco=form["endereco"], uf=form["uf"]
                                , fornecedor_email=form["email"], fornecedor_telefone=form["telefone"])
        fornecedor.save()

        messages.info(request, 'Fornecedor cadastrado com sucesso.')
        
        return render(request, 'app_gestor/cadastro_fornecedor.html')

class DeletarFornecedor(View):
    def get(self,request, fornecedor_id):
        fornecedor = Fornecedores.objects.get(id = fornecedor_id)
        fornecedor.delete()
        messages.info(request, 'Fornecedor deletado com sucesso.')
        return redirect('pagina-lista_fornecedores')
    
class EditarFornecedor(View):
    def get(self, request, id):
        fornecedor = get_object_or_404(Fornecedores, id=id)
        context = {'fornecedor': fornecedor}
        return render(request, 'app_gestor/editar_fornecedor.html', context)
    
    def post(self, request, id):
        fornecedor = get_object_or_404(Fornecedores, id=id)
        fornecedor.nome_empresa = request.POST.get('nome_empresa')
        fornecedor.cnpj = request.POST.get('cnpj')
        fornecedor.inscricao_estadual = request.POST.get('inscricao_estadual')
        fornecedor.inscricao_municipal = request.POST.get('inscricao_municipal')
        fornecedor.endereco = request.POST.get('endereco')
        fornecedor.uf = request.POST.get('uf')
        fornecedor.fornecedor_email = request.POST.get('fornecedor_email')
        fornecedor.fornecedor_telefone = request.POST.get('fornecedor_telefone')

        fornecedor.save()

        messages.success(request, 'Fornecedor atualizado com sucesso.')
        return redirect('pagina-lista_fornecedores')
    
class DeletarProduto(View):
    def get(self, request, produto_id):
        produto = Produtos.objects.get(id = produto_id)
        produto.delete()
        messages.info(request, 'Produto deletado com sucesso.')
        return redirect('pagina-lista_produtos')

class EditarProduto(View):
    def get(self, request, id):
        produto = get_object_or_404(Produtos, id=id)
        
        context = {'produto': produto}
        
        return render(request, 'app_gestor/editar_produto.html', context)
    
    def post(self, request, id):
        produto = get_object_or_404(Produtos, id = id)
        
        produto.nome_produto = request.POST.get('nome_produto')
        produto.ref = request.POST.get('ref')
        produto.marca = request.POST.get('marca')
        produto.categoria = request.POST.get('categoria')
        produto.localizacao = request.POST.get('localizacao')
        produto.validade = request.POST.get('validade')
        produto.codigo = request.POST.get('codigo')
        produto.quantidade = request.POST.get('quantidade')
        produto.quantidade_alerta = request.POST.get('quantidade_alerta')
        produto.codigo_barras = request.POST.get('codigo_barras')
        produto.preco_compra = request.POST.get('preco_compra')
        produto.descricao = request.POST.get('descricao')

        produto.save()

        return redirect('pagina-lista_produtos')
