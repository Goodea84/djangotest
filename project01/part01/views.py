from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.core.exceptions import *

def index(request):
    return render(request, 'part01/index.html')

def crud(request):
    return render(request, 'part01/crud.html')

def insert(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    area = request.POST.get('area')
    result = ''
    try:
        Employee.objects.create(name=name,email=email,area=area)
        result = 'OK'
    except Exception:
        result = 'NG'
    return render(request, 'part01/crud.html', {'result':result})
