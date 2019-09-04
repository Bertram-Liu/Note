from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('投票首页')

def detail(request,id):
    return HttpResponse(id+'号问题详情')

def result(request,id):
    return HttpResponse(id+'号问题结果')