from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20,unique=True,db_index=True)
    age = models.IntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return '%s.%s' % (self.id,self.name)


class Book(models.Model):
    title = models.CharField(max_length=30,unique=True,db_index=True)
    pub_date = models.DateTimeField(db_index=True)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    website = models.CharField(max_length=30)
