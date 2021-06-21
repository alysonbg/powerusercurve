from datetime import date

import pytest

from poweruserproject.api.models import UserActivity


@pytest.fixture
def user_activity(db):
    return UserActivity.objects.create(
        user_id=1,
        date=date(2021, 6, 19,),
        used=True
    )


def test_create_user_activity(user_activity):
    assert UserActivity.objects.exists()


def test_str(user_activity):
    assert str(user_activity) == '1 - 2021-06-19'
