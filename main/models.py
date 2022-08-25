from unicodedata import name
from django.db import models
#from model_utils import Choices


# Create your models here.
class Post(models.Model):
    name = models.TextField(max_length=10)
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
