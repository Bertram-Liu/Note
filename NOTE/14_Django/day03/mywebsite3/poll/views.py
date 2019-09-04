from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    quest_list = Questions.objects.all()
    return render(request,'index.html',locals())

def detail(request,id):
    return HttpResponse(id+'号问题详情')

def result(request,id):
    return HttpResponse(id+'号问题结果')