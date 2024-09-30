from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("courses/", views.ListCourses.as_view(), name="list_courses"),
]
