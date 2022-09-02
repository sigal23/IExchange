from unicodedata import name
from django.db import models
from django.shortcuts import reverse
#from django.contrib.auth import get_user_model
#from model_utils import Choices


# Create your models here.
class Post(models.Model):
    user = models.TextField(max_length=40, default='admin')
    # if wwe will delete user - all the post of this user will delete
    name = models.TextField(max_length=10)
    phone_number = models.TextField(default=None, blank=True, null=True, max_length=10)
    CUR = (('Shekel', '₪'), ('Dollar', '$'), ('Euro', '€'))
    cur_to_get = models.CharField(choices=CUR, blank=True, max_length=20)
    cur_to_give = models.CharField(choices=CUR, blank=True, max_length=20)
    amount = models.IntegerField()
    AREAS = (('North', 'North'), ('South', 'South'), ('Center', 'Center'))
    area =  models.CharField(choices=AREAS, blank=True, max_length=20)
    city = models.TextField(max_length=40)
    comment = models.TextField(default=None, blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')