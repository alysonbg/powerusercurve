import pytest


@pytest.fixture
def response_users_count(db, auth_client, user_activities):
    return auth_client.get('/api/users/activities/?day=2021-05-02')


def test_status_code(response_users_count):
    assert response_users_count.status_code == 200


def test_response_body(response_users_count):
    assert {'quantity': 1} == response_users_count.data
