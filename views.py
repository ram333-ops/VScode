from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Categoria
from .forms import ComentarioForm


# Página de inicio: posts paginados
def index(request):
    posts_qs = Post.objects.filter(publicado=True).select_related('categoria')
    paginator = Paginator(posts_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categorias = Categoria.objects.all()
    return render(request, 'blog/index.html', {
         'page_obj': page_obj,
         'categorias': categorias,
    })

def por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    posts_qs = Post.objects.filter(publicado=True, categoria=categoria)
    paginator = Paginator(posts_qs, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    categorias = Categoria.objects.all()
    return render(request, 'blog/index.html', {
         'page_obj': page_obj,
         'categorias': categorias,
         'categoria_activa': categoria,
    })

def buscar(request):
    q = request.GET.get('q', '').strip()
    posts_qs = Post.objects.filter(publicado=True)
    if q:
        posts_qs = posts_qs.filter(Q(titulo__icontains=q) | Q(cuerpo__icontains=q) | Q(resumen__icontains=q))
    paginator = Paginator(posts_qs, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    categorias = Categoria.objects.all()
    return render(request, 'blog/index.html', {
         'page_obj': page_obj,
         'categorias': categorias,
         'q': q,
    })

def detalle(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    comentarios = post.comentarios.filter(activo=True)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
          nuevo = form.save(commit=False)
          nuevo.post = post
          nuevo.save()
          return redirect('blog:detalle', slug=post.slug)
    else:
        form = ComentarioForm()

    categorias = Categoria.objects.all()
    return render(request, 'blog/detail.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form,
        'categorias': categorias,
    })

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt # en producción, gestionar CSRF correctamente
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    post.likes = (post.likes or 0) + 1
    post.save(update_fields=['likes'])
    return JsonResponse({'ok': True, 'likes': post.likes})


# Create your views here.
