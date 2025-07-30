import pytest
from django.contrib.auth.models import User
from api.models import PatientProfile, ClinicalTrial, Bookmark
from api.serializers import PatientProfileSerializer, ClinicalTrialSerializer, BookmarkSerializer

@pytest.mark.django_db
def test_patient_profile_serializer():
    user = User.objects.create_user(username='testuser', password='testpass')
    profile = PatientProfile.objects.create(user=user, age=30, gender='Male', condition='Hypertension', medications='None')
    serializer = PatientProfileSerializer(profile)
    data = serializer.data

    assert data['user'] == user.id
    assert data['age'] == 30
    assert data['gender'] == 'Male'
    assert data['condition'] == 'Hypertension'

@pytest.mark.django_db
def test_clinical_trial_serializer():
    trial = ClinicalTrial.objects.create(
        title='Trial A',
        inclusion_criteria='Age 18-65',
        exclusion_criteria='Heart conditions',
        location='New York'
    )
    serializer = ClinicalTrialSerializer(trial)
    data = serializer.data

    assert data['title'] == 'Trial A'
    assert 'inclusion_criteria' in data
    assert 'location' in data

@pytest.mark.django_db
def test_bookmark_serializer():
    user = User.objects.create_user(username='markuser', password='pass')
    trial = ClinicalTrial.objects.create(title='Trial B', inclusion_criteria='Any', exclusion_criteria='None', location='Delhi')
    bookmark = Bookmark.objects.create(user=user, trial=trial)
    serializer = BookmarkSerializer(bookmark)
    data = serializer.data

    assert data['user'] == user.id
    assert data['trial'] == trial.id
