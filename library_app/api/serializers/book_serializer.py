from   rest_framework import serializers
from library_app.api.models.book_model import Book

class BookSerializer(serializers.ModelSerializer):
    reviews=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='review-detail')

    class Meta:
        model = Book
        #exclude = ('libraries',)
        fields = '__all__'