from django.shortcuts import render

# Create your views here.
def teste(request):
    return render(request, 'gos/paginas/create.html')