from django.contrib.auth.models import AbstractUser
from django.db import models

from api.managers import CustomUserManager


class Author(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]
    email = models.EmailField(
        'Электронная почта',
        unique=True,
        blank=False,
        max_length=150,
        help_text='Введите вашу электронную почту',
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=False,
        help_text='Введи вашем Имя',
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=False,
        help_text='Введите вашу фамилию',
    )
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
