from contextlib import _RedirectStream
from unicodedata import name
from django.db import models
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
#from model_utils import Choices
from datetime import date

# Create your models here.
class Post(models.Model):
    #user = models.ForeignKey(
    #    settings.AUTH_USER_MODEL,
    #    related_name='written_posts',
    #    on_delete=models.CASCADE)
    #user = models.ForeignKey(User., on_delete=models.CASCADE)
    user = models.CharField(max_length=40, default='admin')
    # if wwe will delete user - all the post of this user will delete
    name = models.TextField(max_length=20)
    phone_number = models.TextField(default=None, blank=True, null=True, max_length=10)
    #CUR = (('Shekel', '₪'), ('Dollar', '$'), ('Euro', '€'))
    cur_to_get = models.CharField(blank=True, max_length=100)
    cur_to_give = models.CharField(blank=True, max_length=100)
    amount = models.IntegerField()
    #AREAS = (('North', 'North'), ('South', 'South'), ('Center', 'Center'))
    area =  models.CharField(blank=True, max_length=100)
    city = models.TextField(max_length=40)
    comment = models.TextField(default=None, blank=True, null=True, max_length=200)
    created_date = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/"