from django.shortcuts import render

def pagina1(request):
    return render(request, "pagina1.html")

def pagina2(request):
    return render(request, "pagina2.html")

def pagina3(request):
    return render(request, "pagina3.html")

def pagina4(request):
    return render(request, "pagina4.html")