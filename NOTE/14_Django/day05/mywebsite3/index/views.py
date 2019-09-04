from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def oto_views(request):
    #增加舒夫人到wife 表 关联老舍的数据
    # wife = Wife()
    # wife.name = '舒夫人'
    # wife.age = 18
    # #通过wife表中 author_id 的属性找到对应的Author对象
    # #wife.author_id = 1
    # author = Author.objects.get(name='老舍')
    # wife.author = author
    # wife.save()
    # wife = Wife.objects.get(name='舒夫人')
    # print('夫人姓名:%s,作者姓名:%s' % (wife.name,wife.author.name))

    # wife = Wife.objects.create(name='李夫人',age=18,author_id=2)
    # print('夫人姓名:%s,作者姓名:%s' % (wife.name, wife.author.name))

    wife = Wife.objects.create(name='周夫人', age=18, author_id=3)
    print('夫人姓名:%s,作者姓名:%s' % (wife.name, wife.author.name))

    return HttpResponse('添加Wife完毕')

def oto2_views(request):
    '''
    获取所有的作者和妻子 在模板中展示
    :param request:
    :return:
    '''
    wife_list = Wife.objects.all()
    author_list = Author.objects.all()
    return render(request,'oto.html',locals())

def otm_views(request):
    '''
    实现一对多的查询
    获取所有的图书,展示图书和对应的出版社
    获取所有的出版社,展示出版社和出版的图书
    :param request:
    :return:
    '''
    book_list = Book.objects.all()
    pub_list = Publisher.objects.all()
    pub = pub_list[0]
    books = pub.book_set.all()
    return render(request,'otm.html',locals())

def mtn_views(request):
    book = Book.objects.get(id=1)
    #正向查询 Book-->Author
    print(book.author.all())
    print(book.author.filter(age__gt=60))
    #反向查询 Author-->Book
    laoshe = Author.objects.get(name='老舍')
    print(laoshe.book_set.all())
    return HttpResponse('查询完毕')

