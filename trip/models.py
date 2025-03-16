from django.db import models
from datetime import datetime, timedelta

class Trip(models.Model):
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    current_address = models.CharField(max_length=255, blank=True, null=True) 
    dropoff_location = models.CharField(max_length=255)
    pickup_address = models.CharField(max_length=255, blank=True, null=True) 
    dropoff_address = models.CharField(max_length=255, blank=True, null=True)  
    cycle_hours = models.FloatField()
    total_miles = models.FloatField(default=0)
    status_log = models.JSONField(default=dict)  
    created_at = models.DateTimeField(auto_now_add=True)

    duration = models.FloatField(default=0)  
    fuel_stops = models.JSONField(default=list) 
    water_alerts = models.JSONField(default=list)  
    available_routes = models.JSONField(default=list) 

    def can_start_new_trip(self):
        """Check if driver has exceeded 70-hour rule in the last 8 days."""
        eight_days_ago = datetime.now() - timedelta(days=8)
        recent_trips = Trip.objects.filter(created_at__gte=eight_days_ago)
        
        total_hours = sum(trip.cycle_hours for trip in recent_trips)
        
        return total_hours < 70  

    def __str__(self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location}"
