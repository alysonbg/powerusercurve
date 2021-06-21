from django.urls import path
from poweruserproject.api.views import list_user_activities, list_amount_of_users_for_a_day

urlpatterns = [
    path('users/<int:user_id>/', list_user_activities),
    path('users/activities/', list_amount_of_users_for_a_day),
]
