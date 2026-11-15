from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-data_postagem')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # Retorna 404 se requisitar post inexistente
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        # Sem validação e sem form, pegando direto dos inputs HTML
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        Post.objects.create(titulo=titulo, conteudo=conteudo)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    # Requisição GET renderiza a página de confirmação
    return render(request, 'blog/post_confirm_delete.html', {'post': post})