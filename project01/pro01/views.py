from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pro01/index.html')

def crud(request):
    return render(request, 'pro01/crud.html')

def insert(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    area = request.POST.get('area')
    str = "이름: {}, 이메일: {}, 지역: {}".format(name,email,area)
    return HttpResponse(str)