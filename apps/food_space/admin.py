from django.contrib import admin
from .models import FoodSpace, Image, Review, Reservation, MenuItem, Order, Promotion, Event, OrderedItem


class FoodImageInline(admin.TabularInline):
    model = Image

@admin.register(FoodSpace)
class FoodSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'cuisine', 'price_category')
    list_filter = ('city', 'cuisine', 'price_category')
    search_fields = ('name', 'city')
    inlines = [FoodImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_space')
    list_filter = ('food_space', 'user')
    search_fields = ('user__username', 'food_space__name')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_space', 'date', 'guests')
    list_filter = ('food_space', 'date')
    search_fields = ('user__username', 'food_space__name')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_space', 'price')
    list_filter = ('food_space', 'price')
    search_fields = ('name', 'food_space__name')


class OrderedItemInline(admin.TabularInline):
    model = OrderedItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderedItemInline]
    list_display = ('user', 'food_space', 'order_date', 'is_completed')
    list_filter = ('food_space', 'order_date', 'is_completed')
    search_fields = ('user__username', 'food_space__name')



@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'food_space', 'start_date', 'end_date')
    list_filter = ('food_space', 'start_date', 'end_date')
    search_fields = ('title', 'food_space__name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'food_space', 'start_date', 'end_date')
    list_filter = ('food_space', 'start_date', 'end_date')
    search_fields = ('title', 'food_space__name')

