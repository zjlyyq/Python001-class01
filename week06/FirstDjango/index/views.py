from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Person

# Create your views here.
def index(req):
    return HttpResponse('hello World')

def year(req, year):
    print(year)
    return HttpResponse(year)

# **kargs 获取不定长参数
def name(req, **kargs):
    print(kargs)
    return HttpResponse(kargs['name'])

def myyear(req, year):
    print(req, year)
    # ylist = Person.objects.all()
    ylist = [1,2,3] 
    print(ylist)
    return render(req, 'year.html', locals())

def notfound(req):
    return HttpResponseNotFound("404")

def direct(req):
    return redirect('2020.html')