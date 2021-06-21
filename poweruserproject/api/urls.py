from django.urls import path
from poweruserproject.api import views


urlpatterns = [
    path('users/<int:user_id>/', views.list_user_activities),
    path('users/activities/', views.list_amount_of_users_for_a_day),
    path('users/activities/month/', views.list_daily_activities_for_a_month),
]
