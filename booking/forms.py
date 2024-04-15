from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date

from .models import Booking

class BookingForm(forms.ModelForm):
    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': date.today().isoformat()}
        ),
        initial=date.today()
    )

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Book Table'))

    class Meta:
        model = Booking
        fields = [
            'name',
            'email',
            'guest_count',
            'table',
            'requested_date',
            'requested_time'
        ]

        widgets = {
            'requested_time': forms.Select(),
            'email': forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'})
        }
