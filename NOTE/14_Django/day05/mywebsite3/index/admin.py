from django.contrib import admin
from .models import Author,Book,Publisher
# Register your models here.
#声明管理器类
class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age','email','isActive']
    list_display_links = ['id','name','email']
    list_editable = ['age']
    list_filter = ['isActive']
    search_fields = ['name','email']

    #fields = ['name','email','age']

    fieldsets = [
        ('基本选项',
         {
             'fields':('name','age'),
             'classes':('collapes')
         }),
        ('可选选项',
         {
             'fields':('email','isActive'),
             'classes':('collapes')
         })
    ]


class BookManager(admin.ModelAdmin):
    date_hierarchy = 'pub_date'


class PublisherManager(admin.ModelAdmin):
    list_display = ['name','city','address']
    list_editable = ['address']
    list_filter = ['city']
    search_fields = ['name','address']
    fieldsets = [
        ('基本字段',{
             'fields':('name','city')
         }),
        ('高级字段',{
             'fields':('address','website')
        })
    ]



#注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Author,AuthorManager)
admin.site.register(Book,BookManager)
admin.site.register(Publisher,PublisherManager)