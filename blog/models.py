from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,default='')
    author= models.EmailField(max_length=50,default='')
    content = models.TextField()
    slug = models.CharField(max_length=130,default=50)
    timestamp = models.DateTimeField(blank=True)


class BlogComment(models.Model): 
    sno  = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post  = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp  = models.DateTimeField(default=now)