from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PatientProfileViewSet, MyHealthProfileView
from .views import ClinicalTrialViewSet
from .views import PublicClinicalTrialListView



# Router for admin-level profile management
router = DefaultRouter()
router.register(r'profiles', PatientProfileViewSet)

router.register(r'trials', ClinicalTrialViewSet, basename='clinicaltrial')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    # Authenticated user can create/view/update their own profile
    path('my-profile/', MyHealthProfileView.as_view(), name='my-profile'),

    # Include the router endpoints for admin views
    path('', include(router.urls)),

    path('public-trials/', PublicClinicalTrialListView.as_view(), name='public-trials'),
]
