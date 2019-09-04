from django.contrib import admin
from .models import *
# Register your models here.
class QuestionManager(admin.ModelAdmin):
    list_display = ['id','quest']


class AnswerManager(admin.ModelAdmin):
    list_display = ['id','quest','answer','total']

admin.site.register(Questions,QuestionManager)
admin.site.register(Answers,AnswerManager)