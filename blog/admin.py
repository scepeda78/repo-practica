from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Post.
    Desde http://localhost:8000/admin puedes crear, editar y eliminar posts.
    """
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published',)
    search_fields = ('title', 'author', 'content')
    list_editable = ('published',)
    date_hierarchy = 'created_at'
