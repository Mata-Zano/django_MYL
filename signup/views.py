from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import compraForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    if request.method == 'GET':
        return render(request, 'signupTemplates/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signupTemplates/login.html', {
            'form': AuthenticationForm,
            'error':'Usuario o contraseña incorrecta'
        })

        else:
            login(request, user)
            return redirect('pedido')

        


def signup(request):

    if request.method == 'GET':
        return render(request, 'signupTemplates/signup.html', {
            'form': UserCreationForm,

        })

    else:
        # verificacion de contraseña
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'], email=request.POST['correo'])
                user.save()
                login(request, user)
                return redirect('login')
            except:
                return render(request, 'signupTemplates/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'

                })
        return render(request, 'signupTemplates/signup.html', {
            'form': UserCreationForm,
            'error': 'La contraseña no coinciden'

        })
    
@login_required
def pedido(request):
    if request.method == 'GET':
        return render(request, 'signupTemplates/pedido.html',{
        'form':compraForm
    })
    else:
        try:
            compra = compraForm(request.POST)
            new_compra = compra.save(commit=False)
            new_compra.user = request.user
            new_compra.save()
            return render(request, 'signupTemplates/pedido.html',{
            'form':compraForm,
            'realizado':'El pedido a sido procesado'
            })
        except ValueError:
            return render(request, 'signupTemplates/pedido.html',{
            'form':compraForm,
            'error':'Porfavor ingrese datos validos'
            }) 
    



def salir(request):
    logout(request)
    return redirect('login')
