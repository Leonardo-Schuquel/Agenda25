from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)
    ordering = '-id',  # Ordena os id de forma decrecente
    list_filter = ('created_date',)  # Pesquisa por data de criação
    search_fields = 'id', 'first_name', 'last_name',  # Pesquisa por parametros
    # Cria paginas e delimita quantos contatos vão aparecer por pagina
    list_per_page = 50
    list_max_show_all = 50
    # Permite editar sem ter que entrar no contato
    list_editable = 'phone', 'show',
    list_display_links = 'id', 'first_name', 'last_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = '-id',  # Ordena os id de forma decrecente
