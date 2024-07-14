from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Man'),
        ('W', 'Woman'),
    ]

    email = models.EmailField(blank=False, null=False)
    gender = models.CharField(default='M', choices=GENDER_CHOICES, max_length=1, blank=True)
    city = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    # picture = models.ImageField(upload_to='/user/img/%Y/%m/', blank=True, null=True)
    
    def __str__(self):
        return self.username


