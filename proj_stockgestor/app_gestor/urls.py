from django.urls import path
from . import views


urlpatterns=[
    path('', views.PaginaInicialView.as_view(), name='pagina-inicial'),
    path('registro/', views.registro, name='registro'),
    path('logado/', views.logado, name='logado'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('lista_produtos', views.lista_produtos, name='lista_produtos'),
    path('lista_fornecedores', views.lista_fornecedores, name='lista_fornecedores'),
    path('login/', views.login, name='login'),
]