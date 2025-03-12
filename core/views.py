import logging
logger = logging.getLogger(__name__)
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.http import HttpResponse  # Importa HttpResponse
from . import views


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Permite el acceso a usuarios no autenticados

    def post(self, request, *args, **kwargs):
        logger.info("RegisterView: Petición POST recibida")
        logger.info(f"RegisterView: Datos recibidos: {request.data}") # Log de los datos

        return self.create(request, *args, **kwargs)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    def verify_email(request, token):
        try:
            token = EmailVerificationToken.objects.get(token=token)
            user = token.user
            if not user.email_verified:
                user.email_verified = True
                user.save()
                token.delete() # Eliminar el token después de usarlo
                messages.success(request, '¡Tu correo electrónico ha sido verificado!')
                return redirect('home')  # Redirige a la página principal
            else:
                messages.info(request, 'Tu correo electrónico ya ha sido verificado.')
                return redirect('home')
        except EmailVerificationToken.DoesNotExist:
            messages.error(request, 'Este enlace de verificación no es válido.')
            return redirect('home')

# Para verificar django esta en urls tambien
def home(request):
    return HttpResponse("<h1>¡Hola, Mundo!</h1>")
