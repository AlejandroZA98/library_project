from django.urls import path,include
from library_app.api.views.library_view import LibraryView
from library_app.api.views.list_books_view import ListBook
from library_app.api.views.book_detail import BookDetail
from library_app.api.views.create_book import CreateBook
from library_app.api.views.create_library import CreateLibrary
from library_app.api.views.review_list import ReviewListView
from library_app.api.views.review_detail import ReviewDetail
from library_app.api.views.create_reaview import CreateReview

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('libraries',LibraryView,basename='libraries')

urlpatterns =[
    path('',include(router.urls)),#ver libreri y librerias
    path('books/',ListBook.as_view(),name='books-list'),#ver libros
    path('book-detail/<int:pk>/',BookDetail.as_view(),name='book-detail'),#ver libro
    path('<int:pk>/create-book/',CreateBook.as_view(),name='create-book'),#crear libro
    path('create-library/',CreateLibrary.as_view(),name='create-library'),#crear libreria
    path('review-list/',ReviewListView.as_view(),name='review-list'),
    path('review-detail/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),#ver review
    path('<int:pk>/create-review/',CreateReview.as_view(),name='create-reaview'),
]