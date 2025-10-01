from django.db import models
from django.contrib.auth.models import User


class Refeicao(models.Model):
    comida = models.CharField(max_length= 120)
    def __str__(self):
        return self.comida

class Pedido(models.Model):
    nome = models.CharField(max_length=100)
    prato = models.ForeignKey(Refeicao, on_delete= models.PROTECT)
    observacoes = models.TextField(null= True, blank= True)
    create_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return f"{self.nome_cliente} - {self.prato}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isStaff = models.BooleanField(default=False)

def __str__(self):
    return self.user.username