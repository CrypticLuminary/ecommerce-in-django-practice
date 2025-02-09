from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None,date_of_birth=None,last_name=None,first_name=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an Username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
            last_name=last_name,
            first_name=first_name

        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, email, username, password=None, date_of_birth=None,last_name=None,first_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            date_of_birth=date_of_birth,
            last_name=last_name,
            first_name=first_name

        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class Myuser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    last_name = models.CharField(max_length=30, null=True,blank=True)
    first_name = models.CharField(max_length=30, null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superuser(self):
        return self.is_admin
       
        
        