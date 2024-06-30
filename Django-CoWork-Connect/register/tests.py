from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your tests here.


class AuthenticationViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')

        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_register_view_get(self):
        form_data = {
            "username": 'newuser',
            "email": 'newuser@example.com',
            "password1": "newpassword123",
            "password2": "newpassword123",  # Zgodność haseł
        }
        response = self.client.post(self.register_url, data=form_data)

        # Wyświetlanie błędów formularza
        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(User.objects.filter(username="newuser").exists())
    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_view_post(self):
        login_data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(self.login_url, data=login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")
        self.assertFalse(response.wsgi_request.user.is_authenticated)