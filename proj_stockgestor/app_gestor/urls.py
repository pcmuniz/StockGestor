from django.urls import path
from . import views


urlpatterns=[
    path('', views.PaginaInicialView.as_view(), name='pagina-inicial'),
    path('servicos/', views.PaginaServicosView.as_view(), name='pagina-servicos'),
    path('sobre/', views.PaginaSobreView.as_view(), name='pagina-sobre'),
    path('contato/', views.PaginaContatoView.as_view(), name='pagina-contato'),
    path('registro/', views.RegistroView.as_view(), name='pagina-registro'),
    path('login/', views.LoginView.as_view(), name='pagina-login'),
    path('lista_produtos/', views.ListaProdutosView.as_view(), name='pagina-lista_produtos'),
    path('cadastro_produto/', views.CadastroProdutosView.as_view(), name='pagina-cadastro_produto'),
    path('lista_fornecedores/', views.ListaFornecedoresView.as_view(), name='pagina-lista_fornecedores'),
    path('logado/', views.CadastroFornecedorView.as_view(), name='pagina-cadastro_fornecedor'),
    path('valor_estoque/', views.ValorEstoqueView.as_view(), name='pagina-valor_estoque'),
    # path('delete/<int:id>', views.DeletaFornecedorView.as_view(),name='deleta-fornecedor'),
    path('delete/<int:id>', views.deletaFornecedor,name='deleta-fornecedor'),
]