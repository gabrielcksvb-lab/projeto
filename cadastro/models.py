from django.db import models
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.valor < 0:
            raise ValidationError("Erro: O valor do pedido não pode ser negativo.")

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome}"