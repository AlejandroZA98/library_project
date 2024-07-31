from library_app.api.models.library_model import Library
from library_app.api.serializers.library_serializer import LibrarySerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
#from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly
from rest_framework import viewsets


class LibraryView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Library.objects.all()
    serializer_class=LibrarySerializer
    