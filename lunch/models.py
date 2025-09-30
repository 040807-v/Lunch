from django.db import models
from django.contrib.auth.models import User

class Refeicao(models.Model):
    comida = models.CharField(max_length= 120)
    def __str__(self):
        return self.comida

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    prato = models.ForeignKey(Refeicao, on_delete=models.PROTECT)
    prato_nome = models.CharField(max_length=120, editable=False, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.prato:
            self.prato_nome = self.prato.comida
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario.username} - {self.prato_nome}"
