
from django.urls import path
from . import views
from .views import  CrearPosteo, listar_Noticias, deletecomment


app_name='noticias'
urlpatterns = [
    path('' , listar_Noticias, name='listar.html'),
    path("agregar_posteo/", CrearPosteo.as_view(), name="agregar_posteo"),
    path('post/<int:pk>/', views.post_detail, name='detallenoticias'),
    path('comment/<int:id>/', deletecomment, name='socio_comment'),
]
