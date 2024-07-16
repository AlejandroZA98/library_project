from library_app.api.models.review_model import Review
from library_app.api.serializers.review_serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ReviewDetail(APIView):
    def get(self, request,pk):
        try:
            review=Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error':'No encontrada'},status=status.HTTP_404_NOT_FOUND)
        serializer=ReviewSerializer(review,context={'request': request})
        return Response(serializer.data)
    def put(self, request,pk):
        review=Review.objects.get(pk=pk)
        serializer=ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        review=Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)