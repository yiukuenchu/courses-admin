from django.test import TestCase

from apps.admission.models import Course

# Create your tests here.
class CourseModelTestCase(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(name="Test Course")
        self.assertEqual(course.name, "Test Course")