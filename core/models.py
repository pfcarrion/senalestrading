import logging
import uuid
from datetime import timedelta
from decimal import Decimal

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator, RegexValidator
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField


# Configuración del logger
logger = logging.getLogger(__name__)

#class User(AbstractUser):
#    email_verified = models.BooleanField(default=False)
#    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
#    otp_secret = models.CharField(max_length=255, blank=True, null=True)
#    reset_password_token = models.UUIDField(null=True, blank=True)
#    reset_token_expires = models.DateTimeField(null=True, blank=True)
#    deleted_at = models.DateTimeField(null=True, blank=True)
#
#    groups = models.ManyToManyField(
#        "auth.Group",
#        verbose_name=("groups"),
#        blank=True,
#        help_text=(
#            "The groups this user belongs to. A user will get all permissions "
#            "granted to each of their groups."
#        ),
#        related_name="core_user_groups",  # Cambia esto
#        related_query_name="user",
#    )
#    user_permissions = models.ManyToManyField(
#        "auth.Permission",
#        verbose_name=("user permissions"),
#        blank=True,
#        help_text=("Specific permissions for this user."),
#        related_name="core_user_permissions",  # Cambia esto
#        related_query_name="user",
#    )
#
#    def __str__(self):
#        return self.username

User = get_user_model()  # Obtén el modelo de usuario configurado

class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user.username}"

class Subscription(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('activo', 'Activo'),
        ('prueba', 'Prueba Gratuita'),
        ('pagado', 'Pagado'),
        ('suspendido', 'Suspendido'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    )

    METODOS_PAGO = (
        ('paypal', 'PayPal'),
        ('tarjeta', 'Tarjeta de crédito por PayPal'),
        ('binance', 'Binance'),
        ('gratis', 'Gratis')
    )

    PLANES = (
        ('mensual', 'Mensual'),
        ('trimestral', 'Trimestral'),
        ('semestral', 'Semestral'),
        ('anual', 'Anual')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")

    nombre = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex='^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message='El nombre solo puede contener letras y espacios.')],
        blank=True, null=True  # Permite valores nulos y en blanco
    )

    apellido = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex='^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', message='El apellido solo puede contener letras y espacios.')],
        blank=True, null=True  # Permite valores nulos y en blanco
    )

    pais = CountryField(blank_label='Selecciona un país...')

    correo = models.EmailField(
        max_length=100,
        validators=[EmailValidator(message="Debe ingresar un correo válido.")],
        default='default@example.com'  # Añade un valor predeterminado
    )

    plan = models.CharField(
        max_length=20,
        choices=PLANES,
        null=True, blank=True
    )

    monto = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Monto")
    fecha_inicio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inicio")
    fecha_fin = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Fin")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_pago = models.DateTimeField(null=True, blank=True)

    es_recursiva = models.BooleanField(default=False, verbose_name="Es Recurrente")
    transaction_id = models.CharField(max_length=100, null=True, blank=True, verbose_name="ID de Transacción")
    payer_email = models.EmailField(null=True, blank=True)

    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS_PAGO,
        default='paypal'
    )

    es_prueba_gratuita = models.BooleanField(default=False)
    fecha_expiracion_prueba = models.DateTimeField(null=True, blank=True)

    def verificar_estado(self):
        """Actualizar el estado si la suscripción ha caducado."""
        ahora = timezone.now()

        # Verificar si es una prueba gratuita caducada
        if self.es_prueba_gratuita and self.fecha_expiracion_prueba and ahora > self.fecha_expiracion_prueba:
            self.es_prueba_gratuita = False
            self.estado = "pendiente"  # Requiere pago
            self.plan = None
            self.monto = Decimal("0.00")
            self.save()
            logger.info(f"Suscripción de prueba gratuita caducada para el usuario {self.usuario.email}")

        # Verificar si la suscripción paga ha caducado
        if self.fecha_fin and ahora > self.fecha_fin:
            self.estado = "finalizado"
            self.save()
            logger.info(f"Suscripción pagada caducada para el usuario {self.usuario.email}")

    PRECIOS_PLANES = {
        "mensual": Decimal("10.00"),
        "trimestral": Decimal("25.00"),
        "semestral": Decimal("50.00"),
        "anual": Decimal("100.00"),
    }
    def save(self, *args, **kwargs):
        if self.plan:  # Solo calcular si hay un plan seleccionado
            self.monto = self.PRECIOS_PLANES.get(self.plan, Decimal("0.00"))

        if self.es_prueba_gratuita:
            self.estado = 'prueba'
            if not self.fecha_expiracion_prueba:
                self.fecha_expiracion_prueba = timezone.now() + timedelta(days=1)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
        indexes = [
            models.Index(fields=['usuario', 'estado']),
            models.Index(fields=['plan']),
        ]

    def __str__(self):
        return f"{self.usuario.username} - {self.plan if self.plan else 'Prueba Gratuita'} - {self.estado}"

    def esta_activa(self):
        """Verifica si la suscripción está activa."""
        ahora = timezone.now()
        if self.es_prueba_gratuita:
            return self.fecha_expiracion_prueba >= ahora
        else:
            return self.estado == 'pagado' and (self.fecha_fin is None or self.fecha_fin >= ahora)

    @staticmethod
    def tiene_prueba_gratuita(usuario):
        """Verifica si el usuario ya tiene una suscripción de prueba gratuita."""
        return Subscription.objects.filter(
            usuario=usuario,
            es_prueba_gratuita=True
        ).exists()

    def tiempo_restante_prueba(self):
        """Calcula el tiempo restante de la prueba gratuita."""
        if self.es_prueba_gratuita and self.fecha_expiracion_prueba:
            ahora = timezone.now()
            if self.fecha_expiracion_prueba > ahora:
                return self.fecha_expiracion_prueba - ahora
        return None

    @admin.display(boolean=True, description='¿Está Activa?')
    def es_activa_admin(self):
        """
        Método para mostrar en el admin si la suscripción está activa.
        """
        return self.esta_activa()

    def plan_activo(self):
        """ Verifica si la suscripción sigue activa. """
        if self.es_prueba_gratuita and self.fecha_expiracion_prueba:
            return self.fecha_expiracion_prueba > timezone.now()
        return self.fecha_fin and self.fecha_fin > timezone.now()

    @staticmethod
    def tiene_suscripcion_activa(usuario):
        """Verifica si el usuario ya tiene una suscripción activa."""
        return Subscription.objects.filter(
            usuario=usuario,
            estado__in=["activo", "prueba"]
        ).exists()

    @staticmethod
    def tiene_prueba_gratuita(usuario):
        """Verifica si el usuario ya tiene una prueba gratuita."""
        return Subscription.objects.filter(
            usuario=usuario,
            es_prueba_gratuita=True
        ).exists()
