import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    profileId = models.CharField(max_length=255, default=str(uuid.uuid4()))
    birthdate = models.DateField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"


class Todo(models.Model):
    identifier = models.CharField(max_length=255, verbose_name='Identifier')
    description = models.CharField(max_length=255, verbose_name='Todo description')
    deadline = models.CharField(max_length=255, verbose_name='Deadline')
    shared_from = models.ForeignKey(Person, on_delete=models.CASCADE,related_name="shared_from")
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
