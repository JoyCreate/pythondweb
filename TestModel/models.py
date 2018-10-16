from django.db import models

# Create your models here.
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(u'标题', max_length=50)
    author   = models.CharField(u'作者', max_length=10)
    content= models.CharField(u'正文', max_length=2000)
    post_date = models.DateTimeField(u'发布时间',auto_now_add=True)

    class Meta:
        ordering = ['-post_date']
