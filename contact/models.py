from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# Create your models here.
# first_name (string), last_name(string), phone (string),
# email(email), create_date(date), description(text),
# category (foreign key), show (boolean), owner (foreign key)
# picture (image)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    # Campos obrigatórios
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    # blank=True torna o campo como opcional
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(blank=True)

    # Pega de forma automatica
    created_date = models.DateTimeField(default=timezone.now)
    show = models.BooleanField(default=True)

    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
