from library_app.api.models.review_model import Review
from library_app.api.serializers.review_serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ReviewListView(APIView):
    def get(self, request):
        review=Review.objects.all()
        print(review)
        serializer=ReviewSerializer(review,many=True)
        print(serializer.data)
        return Response(serializer.data)