######## login registratoin app models
from django.db import models
import re
import datetime as dt
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def validate(self,postData):
        error={}
        if len( postData['first_name'] )<3:
            error['first_name']='first_name should be more than 2 chars'
        if len( postData['last_name'] )<3:
            error['last_name']='last_name should be more than 2 chars'
        if not EMAIL_REGEX.match(postData['email']):
            error['email']='email format not valid'
        elif User.objects.filter(email=postData['email']).count()>0:
            error['email']='email taken, sorry!'
        if len(postData['birthday'])<1:
            error['birthday']='birthday cannot be empty'
        else:
            birthday=dt.datetime.strptime(postData['birthday'],"%Y-%m-%d")
            if birthday>dt.datetime.today():
                error['birthday']='you have not been born yet'
            elif dt.datetime.today()- birthday < dt.timedelta(days=365*13):
                error['birthday']='too young too simple'

        if len( postData['password'] )<8:
            error['password']='password cannot be shorter than 8'
        if postData['password']!=postData['password_re']:
            error['password_re']='password not matching'
        
        if len(error)==0:
            pwhash=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())
            print(pwhash)
            User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                birthday=birthday,
                password=pwhash,
            )
            return error
        else:
            return error



    def login(self,postData):
        error={}
        if not EMAIL_REGEX.match(postData['email']):
            error['email_login']='email format not valid'
            return error
        elif User.objects.filter(email=postData['email']).count()==0:
            error['email_login']='login failed'
            return error
        else:
            x=User.objects.get(email=postData['email'])
            x.password
            if bcrypt.checkpw(postData['password'].encode(),x.password.encode()):
                return error
            else:
                error['email_login']='login failed'
                return error


class User(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    email=models.CharField(max_length=35)
    birthday=models.DateTimeField()
    password=models.CharField(max_length=80)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=UserManager()
# Create your models here.
