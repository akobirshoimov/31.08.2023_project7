from django.db import models

# Create your models here.
class Ichimliklar(models.Model):
    name = models.CharField(max_length=120,default = 'coca cola')
    hajmi = models.CharField(max_length=50)
    narhi = models.IntegerField(default = 10000)

    def __str__(self) -> str:
        return self.name

class Korxona(models.Model):
    name = models.CharField(max_length=140,default = ' ')
    build_in = models.DateField(default= '29-08-2023')

    def __str__(self) -> str:
        return self.name
    

