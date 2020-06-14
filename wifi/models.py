from django.db import models
from django.db.models.functions import datetime


class Local(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Password(models.Model):
    location = models.ForeignKey('Local', on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Password: {self.value} for location {self.location.name}'
