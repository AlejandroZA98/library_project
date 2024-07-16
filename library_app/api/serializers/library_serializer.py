from   rest_framework import serializers
from library_app.api.models.library_model import Library

class LibrarySerializer(serializers.ModelSerializer):
    books=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='book-detail')
    #books=serializers.StringRelatedField(many=True)
    class Meta:
        model=Library
        fields='__all__'
