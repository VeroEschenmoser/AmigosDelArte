from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PosteoForm, Post

# Create your views here.
""" def listar_Noticias (request):
    return render (request, 'noticias/listar.html') """

class CrearPosteo(CreateView):
    model = Post
    form_class = PosteoForm
    template_name = 'noticias/agregar_post.html'
    #fields = '__all__'
    #fields = ['titulo', 'contenido']
    def get_success_url(self) -> str:
        return reverse_lazy('Home')

def listar_Noticias(request):
    posts = Post.objects.all()
    post_ordenados = posts.order_by('-fecha')
    return render(request, 'noticias/listar.html', { 'post_noticias': post_ordenados})
