from django.db import models

# Create your models here.
class Posts(models.Model):

    #author_id
    #post_id
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)   
    #post = models.TextField()
    #upload_path = "posts/" + author_id + "/" + post_id + "/"
    #file_of_post = models.FileField(upload_to=upload_path)
    #posted_on_date = models.DateTimeField('Published date')









