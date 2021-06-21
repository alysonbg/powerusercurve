from poweruserproject.api.models import UserActivity
from django.core.management import call_command


def test_importdata(db, mocker):
    get_mock = mocker.patch('poweruserproject.api.management.commands.importdata.get_users_data')
    get_mock.return_value = [{'id': 1, 'activities': [1, 1, 0, 0, 1]}]
    call_command('importdata')
    assert UserActivity.objects.count() == 5
