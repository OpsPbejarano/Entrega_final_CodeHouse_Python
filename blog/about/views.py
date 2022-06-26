from django.shortcuts import render

def about(request):
    return render(request, "about/about.html")

def melina(request):
    return render(request, "about/melina.html")

def pablo(request):
    return render(request, "about/pablo.html")