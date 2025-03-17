from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializers import TripSerializer
import requests
import json
import urllib.parse

ORS_API_KEY = "5b3ce3597851110001cf62486101399094804b8da26a5d913bfcbc0b"
alternative_routes_params = {
    "target_count": 3,  
    "weight_factor": 2, 
    "share_factor": 2 
}

class TripListView(APIView):
    def get(self, request):
        """Fetch all trips sorted by latest"""
        trips = Trip.objects.all().order_by("-created_at") 
        serializer = TripSerializer(trips, many=True)
        
        return Response({
            "recent_trip": serializer.data[0] if serializer.data else None,  
            "all_trips": serializer.data,  
        }, status=status.HTTP_200_OK)


class TripView(APIView):
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            trip = Trip(**serializer.validated_data)

            if not trip.can_start_new_trip():
                return Response({"error": "You have exceeded the 70-hour driving limit."}, status=status.HTTP_400_BAD_REQUEST)
            
            trip.current_address = self.get_address_from_coords(trip.current_location)
            trip.pickup_address = self.get_address_from_coords(trip.pickup_location)
            trip.dropoff_address = self.get_address_from_coords(trip.dropoff_location)

            trip.save()

            route_data = self.get_route_details(trip)

            if route_data.get("routes"): 
                trip.total_miles = route_data["routes"][0]["distance"]
                trip.duration = route_data["routes"][0]["duration"]
                trip.available_routes = route_data["routes"]
                trip.fuel_stops = route_data["fuel_stops"]
                trip.water_alerts = route_data["water_alerts"]
                trip.save()
            else:
                return Response({"error": "No valid routes found."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "trip": TripSerializer(trip).data,  
                "routes": route_data["routes"],
                "fuel_stops": route_data["fuel_stops"],
                "water_alerts": route_data["water_alerts"],
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_address_from_coords(self, latlng):
        """Fetch address from coordinates using OpenRouteService reverse geocoding."""
        lat, lng = latlng.split(",") 
        url = f"https://api.openrouteservice.org/geocode/reverse?api_key={ORS_API_KEY}&point.lat={lat}&point.lon={lng}"
        
        try:
            response = requests.get(url)
            data = response.json()
            if "features" in data and len(data["features"]) > 0:
                return data["features"][0]["properties"]["label"] 
        except Exception as e:
            print(f"Error fetching address: {e}")
        
        return "Unknown Address"

    def get_route_details(self, trip):
        """Fetches multiple routes, fuel stops, and water alerts"""
        start = ",".join(trip.pickup_location.split(",")[::-1])
        end = ",".join(trip.dropoff_location.split(",")[::-1])

    
        alternative_routes_json = json.dumps(alternative_routes_params)
        alternative_routes_encoded = urllib.parse.quote(alternative_routes_json)

        route_url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={ORS_API_KEY}&start={start}&end={end}&alternative_routes={alternative_routes_encoded}"

        response = requests.get(route_url)
        data = response.json()

        if response.status_code != 200:
            print("Error in OpenRouteService response:", data)
            return {"error": "Route fetching failed"}

        print("OpenRouteService API Response:", data)

        routes = []
        if "features" in data and len(data["features"]) > 0:
            for feature in data["features"]:
                if "geometry" in feature and "summary" in feature["properties"]:
                    routes.append({
                        "route": [[lat, lon] for lon, lat in feature["geometry"]["coordinates"]],
                        "distance": feature["properties"]["summary"]["distance"] / 1000,  
                        "duration": feature["properties"]["summary"]["duration"] / 3600, 
                    })

        return {
            "routes": routes,
            "fuel_stops": self.get_fuel_stations(trip.pickup_location, trip.dropoff_location),
            "water_alerts": self.get_water_alerts(trip.pickup_location, trip.dropoff_location),
        }

    def get_fuel_stations(self, start, end):
        """Finds fuel stations between start and end locations"""
        return [
            {"location": "Shell Fuel Station, XYZ City", "distance_from_start": "50km"},
            {"location": "BP Fuel Station, ABC City", "distance_from_start": "120km"},
        ]

    def get_water_alerts(self, start, end):
        """Finds water hazard alerts between start and end"""
        return [
            {"location": "Flooded Area near XYZ Town", "alert_level": "High"},
            {"location": "Heavy Rain near ABC City", "alert_level": "Medium"},
        ]
