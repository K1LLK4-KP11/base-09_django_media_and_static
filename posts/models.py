from django.db import models  

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    avatar = models.ImageField(upload_to='avatars/') 