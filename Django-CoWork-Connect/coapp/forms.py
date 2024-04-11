from django import forms
from .models import Reservation, Desk


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['desk', 'start_date', 'end_date']
        labels = {
            'desk': 'Dostępne biurka',
            'start_date': 'Data początkowa',
            'end_date': 'Data końcowa',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'text', 'autocomplete': 'off'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'text', 'autocomplete': 'off'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        # Aktualizacja queryset dla pola 'desk', aby zawierał atrybut 'data-price' dla każdej opcji
        self.fields['desk'].queryset = Desk.objects.all()
        self.fields['desk'].label_from_instance = self.label_from_instance_with_price

    def label_from_instance_with_price(self, obj):
        # Tutaj definiujemy, jak będzie wyglądała etykieta (i dodatkowe dane) dla każdej opcji w selekcie
        # Uwzględniamy cenę jako atrybut data-price, który zostanie użyty w JavaScript
        return f"{obj.stock_number} - {obj.size} stanowisk, cena: {obj.price} zł/dzień"

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date >= end_date:
            raise forms.ValidationError('Data rozpoczęcia musi być wcześniejsza niż data zakończenia.')

        return cleaned_data
