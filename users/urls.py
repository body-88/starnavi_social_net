from django.urls import path

from users.views.user_activity import UserActivityView


urlpatterns = [
    path("activity/", UserActivityView.as_view()),
]
