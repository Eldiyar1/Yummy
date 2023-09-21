from rest_framework import serializers
from .models import FoodSpace, Image, Review, Reservation, MenuItem, Order, Promotion, Event, OrderedItem
from apps.users.models import CustomUser as User

common_field = serializers.StringRelatedField(label='Общее поле')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'id')


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    food_space = serializers.SlugRelatedField(slug_field='name', queryset=FoodSpace.objects.all())

    class Meta:
        model = Review
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    user = common_field
    food_space = common_field

    class Meta:
        model = Reservation
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderedItemSerializer(many=True, read_only=True)  # Добавьте write_only=True здесь
    price = serializers.SerializerMethodField(label='Общая сумма')
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    food_space = serializers.SlugRelatedField(slug_field='name', queryset=FoodSpace.objects.all())
    order_date = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = Order
        fields = '__all__'

    def get_price(self, obj):
        return obj.get_total_price()


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class FoodSpaceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = FoodSpace
        fields = '__all__'

    def get_average_rating(self, obj):
        return obj.get_average_rating()
