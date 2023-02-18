from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import openai

openai.organization = settings.ORG_ID
openai.api_key = "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"
# Create your views here.

def products(request):
    return render(request, "products.html")

def textgenView(request):
    return render(request, "textgen.html")

def codegenView(request):
    return render(request, "codegen.html")

def imagegenView(request):
    return render(request, "imagegen.html")

def gen(request, model):
    if model == "text":
        response = openai.Completion.create(model="text-davinci-003", prompt=request.GET.get("prompt"), max_tokens=256)
    elif model == "code":
        response = openai.Completion.create(model="code-davinci-002", prompt=request.GET.get("prompt"), max_tokens=256)
    return JsonResponse(response["choices"][0]["text"], safe=False)