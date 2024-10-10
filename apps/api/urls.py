from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("courses/", views.CourseList.as_view(), name="course_list"),
    path("courses/<int:pk>/", views.CourseDetail.as_view(), name="course_detail"),
]
