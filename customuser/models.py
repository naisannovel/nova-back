from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserModelManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Email is required')
        if not name:
            raise ValueError('Name is required')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        print(dir(BaseUserManager))
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUserModel(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    objects = CustomUserModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

