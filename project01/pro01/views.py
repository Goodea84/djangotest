from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pro01/index.html')