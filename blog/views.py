from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    """
    Vista de inicio: muestra todos los posts publicados.
    
    Cuando alguien entra a http://localhost:8000/
    Django ejecuta esta función y le envía la lista de posts al template.
    """
    # Obtiene todos los posts publicados de la base de datos
    posts = Post.objects.filter(published=True)
    
    # Renderiza el template con los posts
    return render(request, 'blog/index.html', {'posts': posts})


def detail(request, pk):
    """
    Vista de detalle: muestra un solo post.
    
    Cuando alguien entra a http://localhost:8000/post/1/
    Django busca el Post con id=1 y lo envía al template.
    """
    # get_object_or_404: si no existe, muestra una página de error 404
    post = get_object_or_404(Post, pk=pk, published=True)
    
    return render(request, 'blog/detail.html', {'post': post})
