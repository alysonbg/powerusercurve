import datetime

import pytest

from poweruserproject.api.models import UserActivity
from poweruserproject.api.serializers import UserActivitySerializer


@pytest.fixture
def user_activities(db):
    activites = [
        UserActivity(user_id=1,
                     date=datetime.date(2021, 2, 1),
                     used=True),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 2, 2),
                     used=True),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 2, 3),
                     used=False),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 2, 4),
                     used=True),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 5, 1),
                     used=True),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 5, 2),
                     used=False),
        UserActivity(user_id=1,
                     date=datetime.date(2021, 5, 3),
                     used=True),
        UserActivity(user_id=2,
                     date=datetime.date(2021, 2, 1),
                     used=True),
        UserActivity(user_id=2,
                     date=datetime.date(2021, 5, 1),
                     used=True),
        UserActivity(user_id=2,
                     date=datetime.date(2021, 5, 2),
                     used=False)
    ]
    return UserActivity.objects.bulk_create(activites)


@pytest.fixture
def response_activities_from_a_user(db, user_activities, client):
    return client.get('/api/users/1/')


def test_activities_from_a_user_status_code(response_activities_from_a_user):
    assert response_activities_from_a_user.status_code == 200


def test_activities_from_a_user_response(response_activities_from_a_user, user_activities):
    activities = UserActivity.objects.filter(user_id=1)
    serializer = UserActivitySerializer(activities, many=True)

    assert response_activities_from_a_user.data == serializer.data


def test_status_code_for_nonexistent_user(db, client):
    response = client.get('/api/users/99/')
    assert response.status_code == 404
