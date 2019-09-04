from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    quest_list = Questions.objects.all()
    return render(request,'index.html',locals())


def detail(request,id):
    quest_obj = Questions.objects.get(id=id)
    answer_list = Answers.objects.filter(quest=quest_obj)
    return render(request,'detail.html',locals())

def vote(request):
    answer = request.POST.get('answer')
    # answer = request.POST['answer']
    answer_obj = Answers.objects.get(id=answer)
    answer_obj.total += 1
    answer_obj.save()
    #跳转到结果页 需要Questions
    quest = answer_obj.quest
    #'/poll/1/result'
    return redirect('/poll/' + str(quest.id) + '/result')


def result(request,id):
    quest = Questions.objects.get(id=id)
    answer_list = Answers.objects.filter(quest=quest)
    return render(request,'result.html',locals())