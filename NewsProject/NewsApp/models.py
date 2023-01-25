from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=30, blank=True , null=True)

    email 		= models.EmailField(unique=True, blank=True , null=True)

    password    = models.CharField(max_length=255,default="" , blank=True , null=True)

    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')

    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')

   
    USERNAME_FIELD 	='email'
    objects 		= CustomUserManager()
    
    def __str__(self):
        return self.email  
class News_submit(models.Model):
    title = models.CharField(max_length=255)
    news_para = models.TextField()
    user_id = models.ForeignKey(User , on_delete=models.CASCADE ,blank=True,null=True )
    is_live = models.IntegerField(default=0)