from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    STATUS_CHOICES = [
    ('d', 'Delivered'),
    ('p', 'Placed'),
    ('s', 'Shipped'),
    ('r','Return'),
    ]

    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='Draft')
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
