from django.urls import path, include
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter
from .views import PatientProfileViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = DefaultRouter()
router.register(r'profiles', PatientProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
