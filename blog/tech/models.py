from django.db import models
from django.contrib.auth.models import User
# from django.db.models.deletion import CASCADE
# Create your models here.
class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    


class Post(models.Model):
    title=models.CharField(max_length=300)
    overview=models.TextField()
    time_upload=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnaill=models.ImageField(upload_to='thumbnails')
    
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    message=models.TextField()
    time_upload=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    

