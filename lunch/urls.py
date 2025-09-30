from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.pedido, name= 'pedido'),
    path('add/', views.add_pedido, name= 'add_pedido'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]