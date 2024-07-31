from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library_app.api.models.library_model import Library
from library_app.api.serializers.library_serializer import LibrarySerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class CreateLibrary(APIView):
    permission_classes=[IsAdminUser]

    def post(self, request):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)