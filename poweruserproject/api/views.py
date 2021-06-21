from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from poweruserproject.api.models import UserActivity
from poweruserproject.api.serializers import UserActivitySerializer


@api_view(['GET'])
def list_user_activities(request, user_id):
    activities = UserActivity.objects.filter(user_id=user_id)
    if not activities:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserActivitySerializer(activities, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_amount_of_users_for_a_day(request):
    day = request.query_params.get('day')
    users_count = UserActivity.objects.filter(date=day, used=True).count()
    return Response({'quantity': users_count}, status=status.HTTP_200_OK)
