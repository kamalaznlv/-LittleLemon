from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Handles GET (list) and POST (create) for menu items
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer 

# Handles GET (retrieve), PUT (update), and DELETE for a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
