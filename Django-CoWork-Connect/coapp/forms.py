from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reservation, Logo

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        today = timezone.localdate()
        if start_date < today:
            raise ValidationError('Data rezerwacji nie może być wcześniejsza od dzisiejszej.')
        return start_date

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date and end_date and end_date <= start_date:
            raise ValidationError('Data zakończenia musi być późniejsza niż data rozpoczęcia.')
        return end_date