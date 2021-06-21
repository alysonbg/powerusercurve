import pytest

from poweruserproject.api.models import UserActivity
from poweruserproject.api.serializers import UserActivitySerializer


@pytest.fixture
def response_activities_from_a_user(db, user_activities, auth_client):
    return auth_client.get('/api/users/1/')


def test_activities_from_a_user_status_code(response_activities_from_a_user):
    assert response_activities_from_a_user.status_code == 200


def test_activities_from_a_user_response(response_activities_from_a_user, user_activities):
    activities = UserActivity.objects.filter(user_id=1)
    serializer = UserActivitySerializer(activities, many=True)

    assert response_activities_from_a_user.data == serializer.data


def test_status_code_for_nonexistent_user(db, auth_client):
    response = auth_client.get('/api/users/99/')
    assert response.status_code == 404
