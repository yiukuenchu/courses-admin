from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from apps.admission.models import Course
from rest_framework.authtoken.models import Token
from rest_framework import status


class ListCoursesTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(name='Test Course')
        self.url = reverse('api:list_courses')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    # 401 Unauthorized
    def test_get_courses_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 200 OK
    def test_get_courses_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Course")
