from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.http import require_POST

#添加session
def add_session(request):
    request.session['mysession'] = 100
    return HttpResponse('添加session成功')

#查询session
def show_session(request):
    mysession = request.session.get('mysession','没有值')
    print('mysession:'+str(mysession))
    return HttpResponse('mysession:'+str(mysession))

#修改sessionurl(r'^mod_session/(\d+)$',views.mod_session),
def mod_session(request,new):
    request.session['mysession'] = new
    return HttpResponse('修改session成功 <a href="/demo/show_session">去查询</a>')

#删除session
def del_session(request):
    del request.session['mysession']
    return HttpResponse('删除session成功 <a href="/demo/show_session">去查询</a>')

def get_view(request):
    return render(request,'ajax-get.html')

def get_server(request):
    uname = request.GET.get('uname')
    uage = request.GET.get('uage')
    return HttpResponse('姓名：%s,年龄：%s' % (uname,uage))

def post_view(request):
    return render(request,'ajax-post.html')

def post_server(request):
    uname = request.POST.get('uname')
    return HttpResponse('传递过来的数据为：'+uname)

def show_view(request):
    print('demo中的show_view视图')
    # raise ValueError('hehe')
    # return render(request,'ajax-get.html')
    def render():
        print('in demo/render')
        return HttpResponse('O98K')

    resp = HttpResponse('OK')
    resp.render = render
    return resp

def upload(request):
    return render(request,'upload.html')

from django.conf import settings
import os

@require_POST
def upload_view(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        #file.name 文件名
        #file.file 文件数据
        filename = os.path.join(settings.MEDIA_ROOT,file.name)
        with open(filename,'wb') as f:
            f.write(file.file.read())
            return HttpResponse('文件接收成功')
    return HttpResponse('文件接收失败')

