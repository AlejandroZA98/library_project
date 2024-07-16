from library_app.api.models.review_model import Review
from library_app.api.serializers.review_serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CreateReview(APIView):
    def post(self, request,pk):
        data=request.data
        data['books']=pk
        
        serializer=ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)