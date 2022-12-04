
from django.urls import path
from . import views
from .views import  CrearPosteo, listar_Noticias


app_name='noticias'
urlpatterns = [
    path('' , listar_Noticias, name='listar.html'),
    path("agregar_posteo/", CrearPosteo.as_view(), name="agregar_posteo"),
]
