from rest_framework import permissions


class ReviewUserOrReadOnly(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        # Permitir siempre las solicitudes de lectura (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:#('GET', 'HEAD', 'OPTIONS') esto se puede cambiar por permissions.SAFE_METHODS
            print(f"Usuario autenticado: {request.user}")
            print(f"Propietario del review: {obj.review_user}")           
            return True
     
        # Permitir solo las solicitudes de escritura (POST, PUT, DELETE) si el usuario es el propietario del objeto
        return obj.review_user == request.user
    
    
class AdminOrReadOnly(permissions.IsAdminUser):# permiso para saber si es admin
    def has_permission(self, request, view):#aqui podemos recibir el objeto al que queremos acceder
        admin_permission = bool(request.user and request.user.is_staff)#verifica si el usuario existe y si el usuario es staff
        return request.method == "GET" and admin_permission #retorna true si el request es get y si admin_permission es true
    