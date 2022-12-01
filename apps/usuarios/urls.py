
from django.urls import path
from . import views



app_name = 'usuarios'

urlpatterns = [
    path('registros/', views.Registro.as_view(), name = 'registro'),
]