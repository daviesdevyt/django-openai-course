from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request, "products.html")

def textgenView(request):
    return render(request, "textgen.html")

def codegenView(request):
    return render(request, "codegen.html")

def imagegenView(request):
    return render(request, "imagegen.html")