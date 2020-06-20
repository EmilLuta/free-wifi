from django.db import models
from django.db.models.functions import datetime


class Local(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    created_at = models.DateField(auto_now=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}; verified = {self.verified}'

    def get_password(self):
        password = Password.objects.filter(location_id=self.id, verified=True).order_by('-id').first()
        if password:
            return password.value
        return f"There is no password available for {self.name}"


class Password(models.Model):
    location = models.ForeignKey('Local', on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'Password: {self.value} for location {self.location.name}; verified = {self.verified}'
