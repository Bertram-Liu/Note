from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名',max_length=20,unique=True,db_index=True)
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱',null=True)
    isActive = models.BooleanField(verbose_name='状态',default=True)

    def __str__(self):
        return '%s.%s' % (self.id,self.name)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'


class Book(models.Model):
    title = models.CharField(max_length=30,unique=True,db_index=True)
    pub_date = models.DateTimeField(db_index=True)
    publisher = models.ForeignKey('Publisher',null=True,on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return '%s-%s' % (self.id,self.title)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    website = models.CharField(max_length=30)
    def __str__(self):
        return '%s-%s' % (self.id,self.name)


class Wife(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    author = models.OneToOneField(Author)
    def __str__(self):
        return self.name



