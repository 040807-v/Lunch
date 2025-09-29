from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido, name= 'pedido'),
    path('add/', views.add_pedido, name= 'add_pedido'),
]