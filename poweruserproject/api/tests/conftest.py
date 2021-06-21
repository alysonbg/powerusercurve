import datetime

import pytest

from poweruserproject.api.models import UserActivity
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


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
                     used=True)
    ]
    return UserActivity.objects.bulk_create(activites)


@pytest.fixture
def auth_client(db):
    user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    token = Token.objects.create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    return client
