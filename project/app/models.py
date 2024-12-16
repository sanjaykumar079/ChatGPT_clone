from django.db import models

# Create your models here.

class Data(models.Model):
  f_name = models.CharField(max_length=100)
  l_name = models.CharField(max_length=100)
  age = models.PositiveIntegerField(default = 0)
  
  def __str__(self):
    return self.f_name