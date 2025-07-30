import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import PatientProfile, ClinicalTrial

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def make_user(username='testuser', password='testpass'):
        return User.objects.create_user(username=username, password=password)
    return make_user

@pytest.fixture
def auth_client(api_client, create_user):
    user = create_user()
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client, user

@pytest.mark.django_db
def test_user_registration(api_client):
    response = api_client.post('/api/register/', {
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'newpass123'
    })
    assert response.status_code == 201
    assert 'username' in response.data

@pytest.mark.django_db
def test_token_login(create_user, api_client):
    create_user(username='loguser', password='logpass')
    response = api_client.post('/api/login/', {
        'username': 'loguser',
        'password': 'logpass'
    })
    assert response.status_code == 200
    assert 'access' in response.data

@pytest.mark.django_db
def test_create_patient_profile(auth_client):
    client, _ = auth_client
    response = client.post('/api/my-profile/', {
        'age': 30,
        'gender': 'Male',
        'condition': 'Asthma',
        'medications': 'Inhaler'
    })
    assert response.status_code in [200, 201]
    assert 'condition' in response.data

@pytest.mark.django_db
def test_public_trial_list(api_client):
    ClinicalTrial.objects.create(
        title='Trial A',
        inclusion_criteria='Age > 18',
        exclusion_criteria='None',
        location='Delhi'
    )
    response = api_client.get('/api/public-trials/')
    assert response.status_code == 200
    assert isinstance(response.data, list)

@pytest.mark.django_db
def test_bookmark_toggle(auth_client):
    client, _ = auth_client
    trial = ClinicalTrial.objects.create(
        title='Trial B',
        inclusion_criteria='Age > 30',
        exclusion_criteria='None',
        location='Mumbai'
    )
    response = client.post(f'/api/bookmarks/{trial.id}/toggle/')
    assert response.status_code in [200, 201]
