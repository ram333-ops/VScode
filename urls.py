from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
path('', views.index, name='index'),
path('categoria/<slug:slug>/', views.por_categoria, name='por_categoria'),
path('post/<slug:slug>/', views.detalle, name='detalle'),
path('buscar/', views.buscar, name='buscar'),
path('post/<slug:slug>/like/', views.like_post, name='like_post'), # AJAX like
]