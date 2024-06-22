from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Użytkownik',
        help_text="Wymagania dla nazwy użytkownika.\nMaksymalnie 150 znaków.\nTylko litery, cyfry i następujące znaki @/./+/-/_.",
        error_messages={
            'required': 'To pole jest wymagane.',
            'invalid': 'Wprowadź poprawną nazwę użytkownika.',
            'unique': 'Użytkownik o takiej nazwie już istnieje.'
        }
    )

    email = forms.EmailField(
        label='Email',
        error_messages={
            'required': 'To pole jest wymagane.',
            'invalid': 'Wprowadź poprawny adres email.'
        }
    )

    password1 = forms.CharField(
        label='Hasło',
        widget=forms.PasswordInput,
        help_text=(
            "<ul>"
            "<li>Twoje hasło nie może być podobne do twoich innych danych osobowych.</li>"
            "<li>Twoje hasło musi zawierać conajmniej 8 znaków.</li>"
            "<li>Twoje hasło nie może być powszechnie używane.</li>"
            "<li>Twoje hasło nie może składać się wyłącznie z cyfr.</li>"
            "</ul>"
        ),
        error_messages={
            'required': _("To pole jest wymagane."),
            'password_too_short': _("Hasło jest zbyt krótkie. Powinno zawierać co najmniej 8 znaków."),
            'password_common': _("Hasło jest zbyt powszechne."),
            'password_entirely_numeric': _("Hasło nie może być całkowicie numeryczne."),
        }
    )
    password2 = forms.CharField(
        label='Potwierdzenie hasła',
        widget=forms.PasswordInput,
        help_text="Wprowadź to samo hasło, co powyżej, w celu weryfikacji.",
        error_messages={
            'required': _("To pole jest wymagane."),
            'password_too_short': _("Hasło jest zbyt krótkie. Powinno zawierać co najmniej 8 znaków."),
            'password_common': _("Hasło jest zbyt powszechne."),
            'password_entirely_numeric': _("Hasło nie może być całkowicie numeryczne."),
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
