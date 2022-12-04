from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField(blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='static/img/')
    fecha = models.DateTimeField(auto_now_add=True)
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('home')


