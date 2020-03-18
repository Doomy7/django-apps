from django.db import models

# Create your models here.
class cvModel(models.Model):
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    education = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
    def __str__(self):
        return self.fname + ' ' + self.sname + ' ' + self.phone + ' ' + self.education + ' ' + self.languages + ' ' + self.details