from library_app.api.serializers.book_serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class CreateBook (APIView):
    permission_classes=[IsAuthenticated]

    def post (self,request,pk):
        data=request.data
        data['libraries']=pk

        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
