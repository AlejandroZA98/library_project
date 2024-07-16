from django.db import models
from library_app.api.models.library_model import Library

class Book(models.Model):
    libraries=models.ForeignKey(Library,on_delete=models.CASCADE,related_name='books')
    title = models.CharField(max_length=100)
    editorial= models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    def __str__(self):
        return self.title