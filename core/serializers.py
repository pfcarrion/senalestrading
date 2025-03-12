from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}) # Asegura que la contraseña sea requerida
    email = serializers.EmailField(required=True) #Asegura que el correo sea obligatorio

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},  # Oculta la contraseña en la respuesta
            'email': {'required': True} #email obligatorio
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Después de crear el usuario, crea el token y envia el correo
        token = EmailVerificationToken.objects.create(user=user)
        send_verification_email(user.email, token.token)
        return user

    def send_verification_email(email, token):
        subject = 'Verifica tu cuenta'
        message = f'Por favor, haz clic en el siguiente enlace para verificar tu cuenta: http://192.168.11.10:8000/verify-email/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("Esta cuenta está inactiva.")
                data['user'] = user
            else:
                raise serializers.ValidationError("Credenciales incorrectas.")
        else:
            raise serializers.ValidationError("Debe incluir el nombre de usuario y la contraseña.")

        return data
