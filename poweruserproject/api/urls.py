from django.urls import path
from poweruserproject.api.views import list_user_activities

urlpatterns = [
    path('users/<int:user_id>/', list_user_activities),
]
