from django.contrib import admin
from .models import Cliente, Pedido

# Registra os modelos no painel Admin
admin.site.register(Cliente)
admin.site.register(Pedido)