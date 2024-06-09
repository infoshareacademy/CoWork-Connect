from django.test import TestCase
from django.contrib.auth.models import User
from coapp.models import Desk, Reservation
from datetime import date
from django.urls import reverse
from .forms import ReservationForm


class DeskModelTest(TestCase):
    def setUp(self):
        self.desk = Desk.objects.create(
            stock_number="B001",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=100.00,
            status="czynne"
        )

    def test_desk_creation(self):
        self.assertEqual(self.desk.stock_number, "B001")
        self.assertEqual(self.desk.size, 4)
        self.assertEqual(self.desk.monitor_number, 2)
        self.assertEqual(self.desk.power_socket_count, 4)
        self.assertEqual(self.desk.price, 100.00)
        self.assertEqual(self.desk.status, "czynne")

    def test_update_status(self):
        self.desk.update_status("zajęte")
        self.assertEqual(self.desk.status, "zajęte")


class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.desk = Desk.objects.create(
            stock_number="B002",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=150.00,
            status="czynne"
        )
        self.reservation = Reservation.objects.create(
            desk=self.desk,
            user=self.user,
            start_date=date(2024, 6, 10),
            end_date=date(2024, 6, 15),
            total_cost=750.00
        )

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.desk, self.desk)
        self.assertEqual(self.reservation.user, self.user)
        self.assertEqual(self.reservation.start_date, date(2024, 6, 10))
        self.assertEqual(self.reservation.end_date, date(2024, 6, 15))
        self.assertEqual(self.reservation.total_cost, 750.00)


class DeskListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.desk = Desk.objects.create(
            stock_number="B001",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=100.00,
            status="czynne"
        )
        self.client.login(username='testuser', password='12345')

    def test_desk_list_view(self):
        response = self.client.get(reverse('desk_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "B001")


class ReserveDeskViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.desk = Desk.objects.create(
            stock_number="B002",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=150.00,
            status="czynne"
        )
        self.client.login(username='testuser', password='12345')

    def test_reserve_desk_view(self):
        response = self.client.post(reverse('reserve_desk', args=[self.desk.id]), {
            'start_date': '2024-06-10',
            'end_date': '2024-06-15'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful reservation
        self.desk.refresh_from_db()
        self.assertEqual(self.desk.status, 'zajęte')


class UserReservationsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.desk = Desk.objects.create(
            stock_number="B003",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=120.00,
            status="czynne"
        )
        self.reservation = Reservation.objects.create(
            desk=self.desk,
            user=self.user,
            start_date=date(2024, 6, 10),
            end_date=date(2024, 6, 12),
            total_cost=360.00
        )
        self.client.login(username='testuser', password='12345')

    def test_user_reservations_view(self):
        response = self.client.get(reverse('user_reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "B003")


class CancelReservationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.desk = Desk.objects.create(
            stock_number="B004",
            size=4,
            monitor_number=2,
            power_socket_count=4,
            price=180.00,
            status="czynne"
        )
        self.reservation = Reservation.objects.create(
            desk=self.desk,
            user=self.user,
            start_date=date(2024, 6, 10),
            end_date=date(2024, 6, 12),
            total_cost=360.00
        )
        self.client.login(username='testuser', password='12345')

    def test_cancel_reservation_view(self):
        response = self.client.get(reverse('cancel_reservation', args=[self.reservation.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful cancellation
        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(id=self.reservation.id)
        self.desk.refresh_from_db()
        self.assertEqual(self.desk.status, 'czynne')


class ReservationFormTest(TestCase):
    def test_reservation_form_valid_data(self):
        form = ReservationForm(data={
            'start_date': '2024-06-10',
            'end_date': '2024-06-12'
        })
        self.assertTrue(form.is_valid())

    def test_reservation_form_invalid_start_date(self):
        form = ReservationForm(data={
            'start_date': '2023-06-10',
            'end_date': '2024-06-12'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['start_date'], ['Data rezerwacji nie może być wcześniejsza od dzisiejszej.'])

    def test_reservation_form_invalid_end_date(self):
        form = ReservationForm(data={
            'start_date': '2024-06-12',
            'end_date': '2024-06-10'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['end_date'], ['Data zakończenia musi być późniejsza niż data rozpoczęcia.'])

from coapp.models import OurOffer
class SingletonModelTestCase(TestCase):
    def test_singleton_creation_and_save(self):
        singleton_instance = OurOffer.load()
        singleton_instance2 = OurOffer.load()
        singleton_instance3 = OurOffer.load()
        self.assertEqual(OurOffer.objects.all().count(), 1)
