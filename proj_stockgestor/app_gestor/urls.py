from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.signup, name='registro'),
]
