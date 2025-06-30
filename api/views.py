from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import PatientProfile
from .serializers import RegisterSerializer, PatientProfileSerializer


class RegisterView(APIView):
    """
    Allows new users to register.
    """
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientProfileViewSet(viewsets.ModelViewSet):
    """
    Admin view for all patient profiles.
    """
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer


class MyHealthProfileView(APIView):
    """
    Authenticated user view to GET, CREATE (POST), and UPDATE (PUT) their own health profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = request.user.patient_profile
            serializer = PatientProfileSerializer(profile)
            return Response(serializer.data)
        except PatientProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # user is set here
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            profile = request.user.patient_profile
        except PatientProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
