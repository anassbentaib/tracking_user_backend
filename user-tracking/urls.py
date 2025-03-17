
from django.contrib import admin
from django.urls import path, include  
from django.conf import settings
from django.http import JsonResponse
from django.urls import path, include


def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', health_check),  
    path('admin/', admin.site.urls),
    path('api/', include('trip.urls')),
]

