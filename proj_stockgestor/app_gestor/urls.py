from django.urls import path
from . import views


urlpatterns=[
    path('', views.PaginaInicialView.as_view(), name='pagina-inicial'),
    path('servicos/', views.PaginaServicosView.as_view(), name='pagina-servicos'),
    path('sobre/', views.PaginaSobreView.as_view(), name='pagina-sobre'),
    path('contato/', views.PaginaContatoView.as_view(), name='pagina-contato'),
    path('registro/', views.RegistroView.as_view(), name='pagina-registro'),
    path('login/', views.LoginView.as_view(), name='pagina-login'),
    path('produtos/', views.ListaProdutosView.as_view(), name='pagina-lista_produtos'),
    path('cadastro_produto/', views.CadastroProdutosView.as_view(), name='pagina-cadastro_produto'),
    path('fornecedores/', views.ListaFornecedoresView.as_view(), name='pagina-lista_fornecedores'),
    path('cadastro_fornecedor/', views.CadastroFornecedorView.as_view(), name='pagina-cadastro_fornecedor'),
    path('valor_estoque/', views.ValorEstoqueView.as_view(), name='pagina-valor_estoque'),
    path('deletar_fornecedor/<int:fornecedor_id>', views.DeletarFornecedor.as_view(),name='deletar-fornecedor'),
    path('deletar_produto/<int:produto_id>', views.DeletarProduto.as_view(), name='deletar-produto'),
    path('detalhes_produto/<int:produto_id>', views.DetalhesProduto.as_view(), name='detalhes-produto'),
]