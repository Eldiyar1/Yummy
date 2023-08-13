from rest_framework import viewsets
from .models import Review, Reservation, Order, UserProfile, Promotion, Event, MenuItem, FoodSpace, OrderedItem
from .serializers import ReviewSerializer, ReservationSerializer, OrderSerializer, \
    UserProfileSerializer, PromotionSerializer, EventSerializer, MenuItemSerializer, FoodSpaceSerializer, \
    OrderedItemSerializer


class FoodSpaceViewSet(viewsets.ModelViewSet):
    queryset = FoodSpace.objects.all()
    serializer_class = FoodSpaceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
