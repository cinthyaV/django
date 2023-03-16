from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

# Esta API Nos devuelve un CRUD completo del usuario
class UserApiViewSet(ModelViewSet):
    # quien puede utilizar los endpoint de UserApiViewSet
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer

    # modelo a trabajar
    queryset = User.objects.all()

    # nos permite registrar un usuario y encriptar la contrasena.
    def create(self, request, *args, **kwargs):
      # Obtiene la contraseña, la encripta
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

  # Nos permite actualizar la password y encriptarla ya creado el usuario.
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
          request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

# Este Endpoint nos permite obtener los datos personales del usuario que esta autenticado y haciendo la peticion.
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)