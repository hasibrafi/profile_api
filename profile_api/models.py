import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfile(models.Model):
    '''Creating User profile'''
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.

    def __str__(self):
        return self.name

    def create_user(self, name, email, password=None):
        '''Create a user profile'''

        if not email:
            raise ValueError('User must have an email address!')
        
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

# class UserProfileManager(BaseUserManager):
#     '''Manager for User profiles'''
#     def create_user(self, email, name, password=None):
#         '''Create a new user profile'''
#         if not email:
#             raise ValueError('User must have an email address!')

#             email = self.normalize_email(email)
#             user = self.model(email=email, name=name)

#             user.set_password(password)
#             user.save(using=self._db)

#             return user

#     def create_superuser(self, email, name, password):
#         '''Creating superuser with given details'''

#         user = self.create_user(email, name, password)

#         user.is_superuser = True
#         user.is_staff = True

#         user.save(using=self._db)

#         return user


# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     '''Database model for Users in the system'''
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_activate = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)

#     objects = UserProfileManager() 

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name

#     def __str__(self):
#         return self.email
