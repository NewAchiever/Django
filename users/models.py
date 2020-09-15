from django.db import models

# Create your models here.
class Users(models.Model):

    #fname. lname. email, password, posts, profile picture, date_of_account
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_on = models.DateTimeField('DateTime when account was made.', auto_now=True)
    user_id = models.AutoField(primary_key = True)


