from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from collections import Counter
from .models import Pedido, Refeicao
from .forms import PedidoForm, SignUpForm

# LISTAGEM DE PEDIDOS
@login_required
def pedido(request):
    pedidos = Pedido.objects.filter(usuario=request.user)  # 🔹 só do usuário logado
    return render(request, 'pedidolist.html', {'pedidos': pedidos})

# ADICIONAR PEDIDO
@login_required
def add_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user  # 🔹 vincula ao usuário logado
            pedido.save()
            return redirect('pedido')
    else:
        form = PedidoForm()
        form.fields['prato'].queryset = Refeicao.objects.all()
    return render(request, 'pedidoform.html', {'form': form})


# ATUALIZAR PEDIDO
@login_required
def update_pedido(request, pk):
    pedido_obj = get_object_or_404(Pedido, pk=pk, usuario=request.user)
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
    pedido_obj = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    if request.method == 'POST':
        pedido_obj.delete()
        return redirect('pedido')
    return render(request, 'pedidodelete.html', {'pedido': pedido_obj})

# RELATORIO
@login_required
def relatorio_pedidos(request):
    pedidos = Pedido.objects.all()
    total_pedidos = pedidos.count()
    pratos_unicos = set(pedido.prato for pedido in pedidos)
    # Lista completa de pedidos
    lista_completa = [
        {
            "nome": pedido.nome,
            "prato": pedido.prato,
            "observacao": pedido.observacoes or ""
        }
        for pedido in pedidos
    ]
    # Resumo por prato
    resumo_por_prato = dict(Counter(pedido.prato for pedido in pedidos))
    context = {
        "total_pedidos": total_pedidos,
        "pratos_unicos": len(pratos_unicos),
        "lista_completa": lista_completa,
        "resumo_por_prato": resumo_por_prato
    }
    return render(request, "relatorio.html", context)


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
            form.save()  # cria o usuário
            return redirect('login')  # 🔹 vai para tela de login
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# LOGIN (apenas renderiza o template)
def user_login(request):
    return render(request, 'login.html')
