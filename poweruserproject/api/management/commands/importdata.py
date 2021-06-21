from django.core.management.base import BaseCommand
import requests
from datetime import date, timedelta
from poweruserproject.api.models import UserActivity


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = get_users_data()

        d1 = date(2021, 1, 1)
        d2 = date(2021, 12, 31)

        dd = [d1 + timedelta(days=x) for x in range((d2 - d1).days + 1)]
        user_activities = []
        for user in users:
            for i, a in enumerate(user['activities']):
                user_activities.append(UserActivity(user_id=user.get('id'),
                                                    date=dd[i],
                                                    used=bool(a)))
        UserActivity.objects.bulk_create(user_activities)

        print('Done!')


def get_users_data():
    return requests.get('https://static.cingulo.com/bi/user_activities.json').json()
