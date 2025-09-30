from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Pedido, Refeicao
from .forms import PedidoForm, SignUpForm

# LISTAGEM DE PEDIDOS
@login_required
def pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidolist.html', {'pedidos': pedidos})

# ADICIONAR PEDIDO
@login_required
def add_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    else:
        form = PedidoForm()
        # Se quiser limitar os pratos disponíveis
        form.fields['prato'].queryset = Refeicao.objects.all()
    return render(request, 'pedidoform.html', {'form': form})

# ATUALIZAR PEDIDO
@login_required
def update_pedido(request, pk):
    pedido_obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido_obj)
        if form.is_valid():
            form.save()
            return redirect('pedido')
    else:
        form = PedidoForm(instance=pedido_obj)
    return render(request, 'pedidoform.html', {'form': form, 'pedido': pedido_obj})

# EXCLUIR PEDIDO
@login_required
def delete_pedido(request, pk):
    pedido_obj = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido_obj.delete()
        return redirect('pedido')
    return render(request, 'pedidodelete.html', {'pedido': pedido_obj})

# LOGOUT
@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

# CADASTRO DE USUÁRIO
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # loga o usuário após cadastro
            return redirect('pedido')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# LOGIN (apenas renderiza o template)
def user_login(request):
    return render(request, 'login.html')
