from django.urls import path

from . import views

app_name = "travel"

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile_view, name="profile"),
]