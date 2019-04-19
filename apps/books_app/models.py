####### books_app models
from django.db import models

from ..login_registration_app.models import User

class BookManager(models.Manager):
    def validate(self,postData):
        error={}
        if len( postData['title'] )<1:
            error['title']='a book must get a title right?'
        if len( postData['desc'] )<5:
            error['desc']='desc cannot be shorter than 5 chars plez'
        return error
    # def is_fav(self,user_id):
    #     if User.objects.get(id=user_id):
    #         if 



class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    creater=models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    favorites=models.ManyToManyField(User,related_name='fav_books')

    objects=BookManager()

# Create your models here.
