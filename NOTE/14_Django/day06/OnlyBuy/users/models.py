from django.db import models

# Create your models here.
class Users(models.Model):
    uname = models.CharField(max_length=20,verbose_name='姓名')
    upwd = models.CharField(max_length=50,verbose_name='密码')
    uemail = models.EmailField(verbose_name='邮箱')
    uphone = models.CharField(max_length=11,verbose_name='手机',unique=True)
    isActive = models.BooleanField(default=True,verbose_name='状态')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'users'
