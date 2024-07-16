from library_app.api.models.library_model import Library
from library_app.api.serializers.library_serializer import LibrarySerializer
from rest_framework import viewsets


class LibraryView(viewsets.ModelViewSet):
    queryset=Library.objects.all()
    serializer_class=LibrarySerializer