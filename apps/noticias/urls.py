
from django.urls import path
from . import views


app_name='noticias'
urlpatterns = [
    path('' ,views.listar_Noticias, name='listar.html'),
]
