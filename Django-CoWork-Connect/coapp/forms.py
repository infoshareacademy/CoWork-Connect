from django import forms
from django.contrib.auth.models import User
from .models import Reservation, Desk

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['desk', 'user', 'start_date', 'end_date', 'total_cost']
        widgets = {
            'desk': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'total_cost': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['desk'].queryset = Desk.objects.filter(status='czynne') # Filtruje biurka tylko o statusie 'czynne'
        self.fields['user'].queryset = User.objects.all() # Jeśli chcesz ograniczyć do określonych użytkowników, zmodyfikuj ten queryset
        # Usuwa pole użytkownika, jeśli chcesz, aby użytkownik był ustawiany automatycznie (np. z request.user w widoku)
        self.fields.pop('user')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Walidacja dat: start_date musi być wcześniejsza niż end_date
        if start_date and end_date and start_date >= end_date:
            raise forms.ValidationError('Data rozpoczęcia musi być wcześniejsza niż data zakończenia.')

        # Tutaj możesz dodać więcej własnych metod walidacji

        return cleaned_data
