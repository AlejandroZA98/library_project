from library_app.api.models.book_model import Book
from library_app.api.serializers.book_serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class ListBook(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True,context={'request': request})
        return Response(serializer.data)
   