from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
import json
# Create your views here.
def register(request):
    '''
    如果是GET请求在注册页面显示表单
    如果是POST请求 将注册的信息录入数据库 返回结果
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'users/register.html',locals())
    else:
        form = RegisterForm(request.POST)
        # print(form)
        if form.is_valid():
            data = form.cleaned_data
            print(data)#返回字典格式的数据
            user = Users(**data)
            try:
                user.save()
                return HttpResponse('注册成功')
            except Exception as e:
                print(e)
                return HttpResponse('注册失败')

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html',locals())
    else:
        # 获取用户提交的账号密码
        uphone = request.POST.get('uphone')
        upwd = request.POST.get('upwd')
        # 去数据库中查找对应的账号
        user = Users.objects.filter(uphone=uphone)
        # 如果找到账号
        if user:
        # 匹配密码成功
            if upwd == user[0].upwd:
        # 将用户数据以列表的形式保存到cookie中
                resp = HttpResponse('登陆成功')
                userinfo = [uphone,upwd]
                user_str = json.dumps(userinfo)
                resp.set_cookie('user',user_str,60*60*24)
                return resp
            else:
            #     失败
            #返回失败信息账号或密码错误
                resp = HttpResponse('账户或密码错误')
                return resp
        else:
            resp = HttpResponse('账户或密码错误')
            return resp
    

def setcookie(request):
   resp =  HttpResponse('增加cookie成功')
   resp.set_cookie('uname','laowang',3600)
   resp.set_cookie('birthday','1988-10-10',3600)
   return resp

def getcookie(request):
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse('获取cookie成功')

def search_view(request):
    if request.method == 'GET':
        #无论是否有查询关键词，都要显示数据
        if 'kw_list' in request.COOKIES:
            kw_list = json.loads(request.COOKIES['kw_list'])
        #判断用户是否提交关键字
        #如果提交关键字 显示与关键字相关的内容
        if 'kw' in request.GET:
            kw_str = '与'+request.GET['kw']+'相关的内容'
        resp = render(request, 'users/search.html', locals())
        #判断kw在不在GET中
        if 'kw' in request.GET:
        #如果有将kw保存到cookie中
        # 判断cookie中是否有kw_list:
            if 'kw_list' in request.COOKIES:
                #cookie中有搜索列表 查重 后续处理
                kw_list = request.COOKIES['kw_list']
                kw_list = json.loads(kw_list)
                kw = request.GET['kw']
                # 查重，判断kw是否已经在列表中，如果不存在将kw追加到列表，再保存到cookies
                if kw not in kw_list:
                    kw_list.append(kw)
                    list_str = json.dumps(kw_list)
                    resp.set_cookie('kw_list', list_str,60*60*24*7)
            else:
                #没有kw_list
                #获取关键词
                kw = request.GET['kw']
                #创建列表 并保存关键词
                kw_list = [kw]
                #将列表转json串
                list_str = json.dumps(kw_list)
                #保存到cookie中
                resp.set_cookie('kw_list',list_str,60*60*24*7)
        return resp

def modcookie(request):
    resp = HttpResponse('将老王的生日改为1999-10-10')
    resp.set_cookie('birthday','1999-10-10',3600)
    return resp

def delcookie(request):
    resp = HttpResponse('删除cookie laowang')
    resp.delete_cookie('uname')
    # print(request.COOKIES['uname'])
    return resp

def setcookiechn(request):
    resp = HttpResponse('设置中文cookie成功')
    uname = '老王'
    #借助json 将uname的值转码存到cookie
    uname = json.dumps(uname)
    print(uname)
    resp.set_cookie('uname',uname,3600)
    # print(request.COOKIES['uname'])
    return resp

def getcookiechn(request):
    if 'uname' in request.COOKIES:
        uname = request.COOKIES['uname']
        uname = json.loads(uname)
        print('uname'+uname)
    return HttpResponse('获取中文cookie成功')


