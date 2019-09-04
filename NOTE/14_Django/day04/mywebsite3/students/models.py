from django.db import models

# Create your models here.
class Classname(models.Model):
    name = models.CharField(max_length=20)

class Students(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField(default=18)
    stu_sex = models.BooleanField(default=1)
    stu_birth = models.DateField()
    stu_create_time = models.DateTimeField()
    stu_score = models.FloatField()
    stu_img = models.ImageField(upload_to='static/images')
    stu_email = models.EmailField(null=True)
    stu_eyes = models.DecimalField(max_digits=7,decimal_places=2,null=True)