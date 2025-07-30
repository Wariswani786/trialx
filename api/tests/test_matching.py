import pytest
from django.contrib.auth.models import User
from api.models import PatientProfile, ClinicalTrial
from api.match_utils import match_trials

@pytest.mark.django_db
def test_match_trials_basic():
    user = User.objects.create_user(username='matcher', password='pass')
    profile = PatientProfile.objects.create(
        user=user,
        age=35,
        gender='Male',
        condition='Hypertension',
        medications='None'
    )

    trial1 = ClinicalTrial.objects.create(
        title='Blood Pressure Study',
        inclusion_criteria='Hypertension',
        exclusion_criteria='Diabetes',
        location='Chennai'
    )

    trial2 = ClinicalTrial.objects.create(
        title='Diabetes Study',
        inclusion_criteria='Diabetes',
        exclusion_criteria='Hypertension',
        location='Mumbai'
    )

    trials = ClinicalTrial.objects.all()

    # match_trials returns list of (trial, score)
    matches = match_trials(profile, trials)

    assert len(matches) == 2
    matched_titles = {match[0].title for match in matches}
    assert 'Blood Pressure Study' in matched_titles
    assert 'Diabetes Study' in matched_titles
