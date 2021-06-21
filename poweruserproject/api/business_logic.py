from django.db.models import Count

from poweruserproject.api.models import UserActivity


def count_daily_activites_for_a_month(month):
    """
    Count how many users have used the app for each day in a month.
    """
    activities = UserActivity.objects.filter(date__month=month, used=True).values('date').annotate(users=Count('id'))
    result = {str(a['date']): a['users'] for a in activities}
    return result


