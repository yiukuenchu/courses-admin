from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from apps.admission.models import Course

from .serializers import CourseSerializer

class ListCourses(APIView):
    serializer_class = CourseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        courses = Course.objects.all()
        serializer = self.serializer_class(courses, many=True)
        return Response(serializer.data)
