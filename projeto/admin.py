from django.contrib import admin
from projeto.models import Cliente, Categoria, Produto

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'telefone', 'cpf',)
    list_display_links = ('id', 'email',)
    search_fields = ('id', 'cpf',)
    list_per_page = 10

admin.site.register(Cliente, ClienteAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id', 'nome',)
    search_fields = ('id', 'nome',)
    list_per_page = 10

admin.site.register(Categoria, CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cor', 'tamanho', 'preco', 'estoque', 'categoria',)
    list_display_links = ('id', 'nome',)
    search_fields = ('id', 'nome',)
    list_per_page = 10

admin.site.register(Produto, ProdutoAdmin)