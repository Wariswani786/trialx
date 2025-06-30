from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PatientProfileViewSet, MyHealthProfileView

# Router for admin-level profile management
router = DefaultRouter()
router.register(r'profiles', PatientProfileViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Authenticated user can create/view/update their own profile
    path('my-profile/', MyHealthProfileView.as_view(), name='my-profile'),

    # Include the router endpoints for admin views
    path('', include(router.urls)),
]
