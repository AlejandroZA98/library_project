from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from library_app.api.models.book_model import Book
from django.contrib.auth.models import User
class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    books=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="reviews")
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__ (self):
         return str(self.rating)+" "+ str(self.books)