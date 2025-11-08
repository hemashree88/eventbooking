from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Booking
from .forms import EventForm, BookingForm

def welcome(request):
    return render(request, 'events/welcome.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            event.available_seats -= booking.tickets
            event.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'events/book_event.html', {'event': event, 'form': form})

def bookings(request):
    all_bookings = Booking.objects.all()
    return render(request, 'events/bookings.html', {'bookings': all_bookings})
