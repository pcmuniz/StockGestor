from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login
from .forms import SignupForm

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