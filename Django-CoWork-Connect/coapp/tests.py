from django.test import TestCase
from coapp.models import SingletonModel

class SingletonModelTestCase(TestCase):
    def test_singleton_creation_and_save(self):
        singleton_instance = SingletonModel.objects.create()
        self.assertIsNotNone(singleton_instance)
        self.assertEqual(singleton_instance.pk, 1)