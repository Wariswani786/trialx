from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import PatientProfile, ClinicalTrial
from .serializers import (
    RegisterSerializer,
    PatientProfileSerializer,
    ClinicalTrialSerializer
)
from .match_utils import match_trials
from .models import Bookmark, ClinicalTrial
from .serializers import BookmarkSerializer


class RegisterView(APIView):
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
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

class MyHealthProfileView(APIView):
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
            serializer.save(user=request.user)
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

class ClinicalTrialViewSet(viewsets.ModelViewSet):
    queryset = ClinicalTrial.objects.all()
    serializer_class = ClinicalTrialSerializer
    permission_classes = [IsAdminUser]

class PublicClinicalTrialListView(generics.ListAPIView):
    queryset = ClinicalTrial.objects.all()
    serializer_class = ClinicalTrialSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'inclusion_criteria']

class MatchTrialsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            profile = user.patient_profile
        except PatientProfile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

        trials = ClinicalTrial.objects.all()
        scored_trials = match_trials(profile, trials)

        # Create response including trial details and match score
        response_data = []
        for trial, score in scored_trials:
            trial_data = ClinicalTrialSerializer(trial).data
            trial_data['match_score'] = score
            response_data.append(trial_data)

        # Return trials sorted by match_score descending
        sorted_response = sorted(response_data, key=lambda x: x['match_score'], reverse=True)
        return Response(sorted_response)


class BookmarkListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookmarks = Bookmark.objects.filter(user=request.user)
        serializer = BookmarkSerializer(bookmarks, many=True)
        return Response(serializer.data)

class ToggleBookmarkView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, trial_id):
        user = request.user
        try:
            trial = ClinicalTrial.objects.get(id=trial_id)
        except ClinicalTrial.DoesNotExist:
            return Response({"detail": "Trial not found."}, status=404)

        bookmark, created = Bookmark.objects.get_or_create(user=user, trial=trial)

        if not created:
            bookmark.delete()
            return Response({"detail": "Bookmark removed."}, status=200)
        return Response({"detail": "Bookmark added."}, status=201)
