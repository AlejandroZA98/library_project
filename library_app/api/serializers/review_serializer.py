from   rest_framework import serializers
from library_app.api.models.review_model import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review

        fields='__all__'