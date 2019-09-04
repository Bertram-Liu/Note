from django.http import HttpResponse

def home(request):
    return HttpResponse(request.is_ajax())

def page1(request):
    return HttpResponse(request.path)

def page2(request):
    return HttpResponse('这是第二个页面')

#接收参数并显示到页面
def page_year(request,year):
    #year对应正则表达式的第一个分组() 2015
    return HttpResponse('当前的年份：' + year)

#接收多个参数
def date(request,year,month,day):
    return HttpResponse(year+'年'+month+'月'+day+'日')

def birthday(request,year,month,day):
    return HttpResponse('生日为：'+year+'年'+month+'月'+day+'日')

def students(request,name,age):
    return HttpResponse('学生姓名：'+name+' 年龄:'+age)

def goods(request,id):
    return HttpResponse('当前查看的是id为'+id+'的商品')