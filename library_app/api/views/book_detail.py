from library_app.api.models.book_model import Book
from library_app.api.serializers.book_serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class BookDetail(APIView):
    def get(self, request, pk):
        try:
            book=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error':'No encontrada'},status=status.HTTP_404_NOT_FOUND)
        serializer=BookSerializer(book,context={'request': request})
        return Response(serializer.data)
    def put(self, request, pk):
        book=Book.objects.get(pk=pk)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book=Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)