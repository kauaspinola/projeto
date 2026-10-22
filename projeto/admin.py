from django.contrib import admin
from projeto.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'telefone', 'cpf',)
    list_display_links = ('id', 'email',)
    search_fields = ('id', 'cpf',)
    list_per_page = 10

admin.site.register(Cliente, ClienteAdmin)