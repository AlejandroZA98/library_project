from django.contrib import admin
from library_app.api.models.library_model import Library
from library_app.api.models.book_model import Book
from library_app.api.models.review_model import Review
# Register your models here.
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Review)