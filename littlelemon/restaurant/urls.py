
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    # Menu APIs
    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    # Booking APIs
    path('bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
]
