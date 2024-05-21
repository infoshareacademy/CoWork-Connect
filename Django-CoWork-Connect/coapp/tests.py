from django.test import TestCase
from coapp.models import OurOffer
class SingletonModelTestCase(TestCase):
    def test_singleton_creation_and_save(self):
        singleton_instance = OurOffer.load()
        singleton_instance2 = OurOffer.load()
        singleton_instance3 = OurOffer.load()
        self.assertEqual(OurOffer.objects.all().count(), 1)