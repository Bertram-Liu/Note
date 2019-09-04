from django.db import models

# Create your models here.
class Questions(models.Model):
    quest = models.CharField(max_length=200,unique=True,db_index=True)
    def __str__(self):
        return '%s.%s' % (self.id,self.quest)


class Answers(models.Model):
    quest = models.ForeignKey('Questions',on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    total = models.IntegerField(default=0)

    def __str__(self):
        return '%s.%s' % (self.answer,self.total)

