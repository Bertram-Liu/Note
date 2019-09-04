from django.contrib import admin
from .models import Author,Book,Publisher
# Register your models here.
#声明管理器类
class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age','email','isActive']


#注册Author模型类时 与 管理器AuthorManager关联
admin.site.register(Author,AuthorManager)
admin.site.register(Book)
admin.site.register(Publisher)