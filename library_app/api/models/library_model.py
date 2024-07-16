from django.db import models

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=100)
    ubication=models.CharField(max_length=200)
    cellphone=models.IntegerField(max_length=10)
    website=models.URLField(max_length=100)
    def __str__(self):
        return self.name