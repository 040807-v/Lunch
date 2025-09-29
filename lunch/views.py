from django.shortcuts import render, redirect
from .models import Pedido, Refeicao
from .forms import PedidoForm, SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidolist.html', {'pedidos': pedidos})

@login_required
def add_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    elif request.method == 'GET':
        refeicao = Refeicao.objects.all()
        form = PedidoForm
        return render(request, 'pedidoform.html', {
            'context': refeicao,
            'form': form
        })
    else:
        form =  PedidoForm()
    return render(request, 'pedidoform.html', {'form': form})

@login_required
def user_login(request):
    return render(request, "login.html")

@login_required
def user_logout(request):
    logout(request) 
    return redirect('login')  

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request) 
            return redirect("pedido")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})