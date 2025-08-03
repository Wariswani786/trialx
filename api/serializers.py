from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientProfile, ClinicalTrial, Bookmark

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

class PatientProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ['user', 'age', 'gender', 'condition', 'medications']

class ClinicalTrialSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(read_only=True)

    class Meta:
        model = ClinicalTrial
        fields = ['id', 'title', 'inclusion_criteria', 'exclusion_criteria', 'location', 'score']

class BookmarkSerializer(serializers.ModelSerializer):
    trial = ClinicalTrialSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'trial', 'created_at']
