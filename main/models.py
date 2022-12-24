from contextlib import _RedirectStream
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=40, default='admin')
    name = models.TextField(max_length=20)
    phone_number = models.TextField(default=None, blank=True, null=True, max_length=10)
    cur_to_get = models.CharField(blank=True, max_length=100)
    cur_to_give = models.CharField(blank=True, max_length=100)
    amount = models.IntegerField()
    area =  models.CharField(blank=True, max_length=100)
    city = models.TextField(max_length=40)
    comment = models.TextField(default=None, blank=True, null=True, max_length=200)
    created_date = models.DateField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/main/personal_post"


# Create your models here.
class Offer(models.Model):
    user = models.CharField(max_length=40, default='admin')
    name = models.TextField(max_length=20)
    phone_number = models.TextField(default=None, blank=True, null=True, max_length=10)
    country = models.CharField(blank=True, max_length=100)
    my_offer = models.TextField(default=None, blank=True, null=True, max_length=200)
    area =  models.CharField(blank=True, max_length=100)
    city = models.TextField(max_length=40)
    comment = models.TextField(default=None, blank=True, null=True, max_length=200)
    created_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/main/personal_offer"
