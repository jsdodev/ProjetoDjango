from django.shortcuts import render

def lista_frutas(request):
    frutas = ['maçã', 'pera', 'uva', 'banana']
    return render(request, 'lista_frutas.html', {'frutas': frutas})

