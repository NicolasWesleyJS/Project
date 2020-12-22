from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    
    def create_user(self, email, date_of_birth, password=None):
        """Creates and Saves a user with email, date of birth and password"""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """Creates and saves a superuser"""
        user = self.create_user(
            email,
            password = password,
            date_of_birth = date_of_birth,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255, 
        unique = True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "does the user have a specific permission?"
        return True
    
    def has_module_perms(self, app_label):
        "does the user have permissions to view the app app_label?"
        return True

    def is_staff(self):
        "is the user a member of staff?"
        return self.is_admin