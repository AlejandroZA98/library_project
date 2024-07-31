from library_app.api.models.review_model import Review
from library_app.api.serializers.review_serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from library_app.api.permission.permissions import ReviewUserOrReadOnly,AdminOrReadOnly
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ReviewListView(APIView):

    permission_classes=[ReviewUserOrReadOnly]
    def get(self, request):
        print("Fr")
        review=Review.objects.all()
        print(review)
        serializer=ReviewSerializer(review,many=True)
        print(serializer.data)
        return Response(serializer.data)