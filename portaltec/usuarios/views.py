from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def logon(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login_index.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return render(request, 'aplicativos/aplicativos_index.html')
        else:
            return render(request, 'usuarios/erro_login.html')


@login_required(login_url='logon')
def aplicativos_index(request):
    return render(request, 'aplicativos/aplicativos_index.html')


def logoff(request):
    logout(request)
    return redirect('index')
