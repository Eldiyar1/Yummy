from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.manager import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    surname = models.CharField(max_length=40)
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(max_length=25, unique=True, verbose_name='Пароль')
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')
    profile = ResizedImageField(size=[300, 300], null=True, blank=True, quality=75)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    code = models.CharField(max_length=6, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['surname', 'password']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    time = models.DateTimeField()
