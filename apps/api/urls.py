from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path("courses/", views.CourseList.as_view(), name="course_list"),
    path("courses/<int:pk>/", views.CourseDetail.as_view(), name="course_detail"),
    path("intakes/", views.IntakeList.as_view(), name="intake_list"),
    path("intakes/<int:pk>/", views.IntakeDetail.as_view(), name="intake_detail"),
]
