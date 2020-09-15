from django.db import models
from datetime import datetime
from users.models import Users

# Create your models here.
class Posts(models.Model):

    post_id = models.AutoField(primary_key = True, blank=True)
    author_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True) #user_id
    title = models.CharField(max_length=50)   
    post = models.TextField(default="No post yet")
    #upload_path = "posts/" + author_id + "/" + post_id + "/"
    #file_of_post = models.FileField(upload_to=upload_path)
    posted_on = models.DateTimeField( 'Published date', auto_now=True)
