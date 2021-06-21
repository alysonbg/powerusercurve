import pytest


@pytest.fixture
def response_daily_activities_from_month(db, auth_client, user_activities):
    return auth_client.get('/api/users/activities/month/?month=5')


def test_status_code(response_daily_activities_from_month):
    assert 200 == response_daily_activities_from_month.status_code


def test_response_body(response_daily_activities_from_month):
    data = {
        '2021-05-01': 2,
        '2021-05-02': 1,
        '2021-05-03': 1,
    }
    assert data == response_daily_activities_from_month.data
