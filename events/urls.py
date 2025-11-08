from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('events/', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('book/<int:pk>/', views.book_event, name='book_event'),
    path('bookings/', views.bookings, name='bookings'),
]
