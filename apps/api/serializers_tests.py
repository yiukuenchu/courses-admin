from datetime import date
from django.test import TestCase

from apps.admission.models import Course, Intake
from apps.api.serializers import CourseSerializer


class CourseSerializerTests(TestCase):
    def setUp(self):
        self.course_data = {
            'name': 'Test Course',
        }
        self.course = Course.objects.create(**self.course_data)
        self.intake1 = Intake.objects.create(
            course=self.course,
            start_date=date(2024, 1, 1),
            end_date=date(2025, 12, 31)
        )
        self.intake2 = Intake.objects.create(
            course=self.course,
            start_date=date(2024, 3, 3),
            end_date=date(2025, 12, 31)
        )
        self.serializer = CourseSerializer(instance=self.course)

    # Test that the serializer contains the expected fields
    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name','intakes']))

    # Test that the name field contains the expected value
    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], 'Test Course')

    # Test that the intakes field contains the expected value
    def test_intakes_field_content(self):
        data = self.serializer.data
        self.assertEqual(len(data['intakes']), 2)
        self.assertEqual(data['intakes'][0]['start_date'], '2024-01-01')
        self.assertEqual(data['intakes'][0]['end_date'], '2025-12-31')
        self.assertEqual(data['intakes'][1]['start_date'], '2024-03-03')
        self.assertEqual(data['intakes'][1]['end_date'], '2025-12-31')

