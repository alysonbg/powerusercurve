import datetime

import pytest

from poweruserproject.api.models import UserActivity


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
