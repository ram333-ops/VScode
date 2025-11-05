from django.contrib import admin
from .models import Categoria, Post, Comentario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = { 'slug': ('nombre',) }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'publicado', 'creado', 'likes')
    list_filter = ('publicado', 'categoria', 'creado')
    search_fields = ('titulo', 'cuerpo')
    prepopulated_fields = { 'slug': ('titulo',) }
    date_hierarchy = 'creado'


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'nombre', 'email', 'activo', 'creado')
    list_filter = ('activo', 'creado')
    search_fields = ('nombre', 'contenido')
    

