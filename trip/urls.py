from django.urls import path
from .views import TripView, TripListView

urlpatterns = [
    path('trips/', TripListView.as_view(), name='trip-list'), 
    path('trips/new/', TripView.as_view(), name='trip-create'),  
]
