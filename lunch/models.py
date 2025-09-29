from django.db import models

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
        return self.nome