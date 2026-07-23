from django.db import models


class Post(models.Model):
    """
    Un post del blog.
    
    Cada campo aquí se convierte en una columna en la tabla 'blog_post'
    de la base de datos PostgreSQL.
    
    ¡MISIÓN: Intenta agregar un nuevo campo aquí, por ejemplo:
    imagen = models.ImageField(upload_to='posts/', blank=True)
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    author = models.CharField(max_length=100, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    published = models.BooleanField(default=True, verbose_name="Publicado")

    class Meta:
        ordering = ['-created_at']  # Más reciente primero
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
