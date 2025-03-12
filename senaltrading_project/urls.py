from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener tokens JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar tokens JWT
    path('', include('core.urls')),  # Incluye las URLs de la app 'core' en la raíz
    path('api/', include('signals.urls')), # Incluye las URLs de la app 'signals' bajo /api/
]
