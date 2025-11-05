from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Categoria(models.Model):
 nombre = models.CharField(max_length=80, unique=True)
 slug = models.SlugField(max_length=100, unique=True, blank=True)


class Meta:
 verbose_name = 'Categoría'
 verbose_name_plural = 'Categorías'
 ordering = ['nombre']


def __str__(self):
 return self.nombre


def save(self, *args, **kwargs):
 if not self.slug:
  self.slug = slugify(self.nombre)
 return super().save(*args, **kwargs)

class Post(models.Model):
 titulo = models.CharField(max_length=200)
 slug = models.SlugField(max_length=220, unique=True, blank=True)
 categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='posts')
 autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
 resumen = models.TextField(max_length=280, blank=True)
 cuerpo = models.TextField()
 creado = models.DateTimeField(auto_now_add=True)
 actualizado = models.DateTimeField(auto_now=True)
 publicado = models.BooleanField(default=True)
 likes = models.PositiveIntegerField(default=0)

 class Meta:
  ordering = ['-creado']


def __str__(self):
 return self.titulo


def save(self, *args, **kwargs):
    if not self.slug:
       base = slugify(self.titulo)
       slug = base
       c = 1
    while Post.objects.filter(slug=slug).exists():
       slug = f"{base}-{c}"
       c += 1
    self.slug = slug
    return super().save(*args, **kwargs)


class Comentario(models.Model):
 post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
 nombre = models.CharField(max_length=80)
 email = models.EmailField()
 contenido = models.TextField()
 creado = models.DateTimeField(auto_now_add=True)
 activo = models.BooleanField(default=True)

 class Meta:
    ordering = ['creado']


 def __str__(self):
    return f"Comentario de {self.nombre} en {self.post}"
 