from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from poweruserproject.api import business_logic
from poweruserproject.api.models import UserActivity
from poweruserproject.api.serializers import UserActivitySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_activities(request, user_id):
    activities = UserActivity.objects.filter(user_id=user_id)
    if not activities:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserActivitySerializer(activities, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_amount_of_users_for_a_day(request):
    day = request.query_params.get('day')
    users_count = business_logic.count_users_per_day(day)
    return Response({'quantity': users_count}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_daily_activities_for_a_month(request):
    month = request.query_params.get('month')
    activities = business_logic.count_daily_activites_for_a_month(month)

    return Response(activities, status=status.HTTP_200_OK)
