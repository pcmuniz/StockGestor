from django.contrib import admin
from django.urls import path
from app_gestor import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("registro/", views.signup, name="registro"),
    path('logado/', views.logado, name="logado"),

]
