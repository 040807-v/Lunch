from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.pedido, name= 'pedido'),
    path('add/', views.add_pedido, name= 'add_pedido'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('update/<int:pk>/', views.update_pedido, name='update_pedido'),
    path('delete/<int:pk>/', views.delete_pedido, name='delete_pedido'),
]