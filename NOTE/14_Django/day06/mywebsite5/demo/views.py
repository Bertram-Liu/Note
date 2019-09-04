from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def demo_views(request):
    # print(request)
    body = request.body
    path = request.path
    schem = request.scheme
    method = request.method
    method_get = request.GET
    method_post = request.POST
    cookies = request.COOKIES
    meta = request.META
    # return HttpResponse('响应完毕')
    return render(request,'request_demo.html',locals())


def post_view(request):
    if request.method == 'GET':
        return render(request,'post.html')
    else:
        #POST请求的内容
        #接收用户提交的数据 打印到终端
        name = request.POST.get('username')
        password = request.POST['password']
        print('用户名：%s，密码：%s' % (name,password))
        return HttpResponse('提交成功！')

def get_view(request):
    #get传递：商品名称 gname
    #        商品价格 gprice
    #        商品数量 count
    #显示：您购买了x件xxx商品, 总价为xxx
    #http://127.0.0.1:8000/demo/get_view/?gname=手机&gprice=6000&count=2
    if request.method == 'GET':
        gname = request.GET.get('gname')
        gprice = int(request.GET.get('gprice'))
        count = int(request.GET.get('count'))
        print('您购买了%d件%s，总价为%d' % (count,gname,gprice*count))
        return HttpResponse('成功！')


def remark(request):
    form = RemarkForm()
    return render(request,'remark_form.html',locals())
