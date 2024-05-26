from django.test import TestCase
from coapp.models import OurOffer, ServiceTerm
class SingletonModelTestCase(TestCase):
    def test_singleton_creation_and_save(self):
        singleton_instance = OurOffer.load()
        singleton_instance2 = OurOffer.load()
        singleton_instance3 = OurOffer.load()
        self.assertEqual(OurOffer.objects.all().count(), 1)

    def test_singleton_creation_and_save(self):
        singleton_instance = ServiceTerm.load()
        singleton_instance2 = ServiceTerm.load()
        singleton_instance3 = ServiceTerm.load()
        self.assertEqual(ServiceTerm.objects.all().count(), 1)