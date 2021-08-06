
from timestamp.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class Organisation(TimeStampedModel):
    license_key = models.UUIDField(primary_key=True,default=uuid.uuid4) 
    email = models.EmailField(_('email address'), unique=True,default="#")
    def __str__(self):
    	return str(self.license_key)


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
      
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser,TimeStampedModel):
    ROLES = (
        ('Manager','Manager'),
        ('Supervisor','Supervisor'),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('Password'),max_length=150)
    roles = models.CharField(max_length=30,choices=ROLES)
    org = models.OneToOneField(Organisation,on_delete=models.CASCADE,blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()