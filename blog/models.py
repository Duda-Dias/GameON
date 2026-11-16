from django.contrib import admin
from django.contrib.auth.models import User


from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    imagem_url = models.URLField(max_length=500, blank=True, null=True)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} no post {self.post.titulo}'