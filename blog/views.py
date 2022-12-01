from django.shortcuts import render

def Home (request):
    return render( request, 'Home.html')

def Quienes (request):
    return render( request, 'Quienes.html')