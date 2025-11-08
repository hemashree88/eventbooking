from django import forms
from .models import Event, Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'tickets']
