from django.urls import path
from . import views


urlpatterns=[
    path('', views.PaginaInicialView.as_view(), name='pagina-inicial'),
    path('registro/', views.RegistroView.as_view(), name='pagina-registro'),
    path('login/', views.LoginView.as_view(), name='pagina-login'),
    path('lista_produtos', views.ListaProdutosView.as_view(), name='pagina-lista_produtos'),
    path('cadastro_produto/', views.CadastroProdutosView.as_view(), name='pagina-cadastro_produto'),
    path('lista_fornecedores', views.ListaFornecedoresView.as_view(), name='pagina-lista_fornecedores'),
    path('logado/', views.CadastroFornecedorView.as_view(), name='pagina-cadastro_fornecedor'),
]