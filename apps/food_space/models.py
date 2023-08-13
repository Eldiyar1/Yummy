from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.contrib.auth.admin import User

from apps.food_space.constants import FOOD_SPACE_AMENITIES_CHOICES, FOOD_SPACE_TYPE_CHOICES, CUISINE_CHOICES, \
    MEAL_CHOICES, PRICE_CHOICES, RATING_CHOICES


class FoodSpace(models.Model):
    class Meta:
        verbose_name = "Место питания"
        verbose_name_plural = "Места питания"

    food_space_type = models.CharField(max_length=50, choices=FOOD_SPACE_TYPE_CHOICES, verbose_name="Тип места питания")
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    city = models.CharField(max_length=100, verbose_name="Город")
    cuisine = models.CharField(choices=CUISINE_CHOICES, max_length=100, verbose_name="Кухня")
    meal_options = MultiSelectField(choices=MEAL_CHOICES, max_length=100, verbose_name="Прием пищи")
    opening_hours = models.TimeField(verbose_name="Часы открытия")
    closing_hours = models.TimeField(verbose_name="Часы закрытия")
    amenities = MultiSelectField(choices=FOOD_SPACE_AMENITIES_CHOICES, max_length=255, verbose_name="Удобства")
    price_category = models.CharField(max_length=20, choices=PRICE_CHOICES, verbose_name="Категория цен")

    def __str__(self):
        return self.name

    def get_average_rating(self):
        ratings = Review.objects.filter(food_space=self)
        if ratings:
            total_rating = sum([
                (rating.staff_rating + rating.food_quality_rating +
                 rating.ambiance_rating + rating.service_rating) / 4
                for rating in ratings
            ])
            average_rating = total_rating / len(ratings)
            return round(average_rating, 1)
        return 0


class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение места питания'
        verbose_name_plural = 'Изображения места питания'

    image = models.ImageField(upload_to='food_spaces', verbose_name='Изображение')
    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Изображение места питания {self.food_space.name}"


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')
    staff_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка персонала")
    food_quality_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка качества пищи")
    ambiance_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка атмосферы")
    service_rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name="Оценка обслуживания")
    comment = models.TextField(max_length=500, blank=True, null=True, verbose_name='Комментарий')

    def __str__(self):
        return f"Отзыв от {self.user} на {self.food_space}"


class Reservation(models.Model):
    class Meta:
        verbose_name = 'Бронь столика'
        verbose_name_plural = 'Бронь столиков'

    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateTimeField(verbose_name='Дата и время')
    guests = models.PositiveIntegerField(verbose_name='Количество гостей')

    def __str__(self):
        return f"Бронь столика в {self.food_space} на {self.date}"


class MenuItem(models.Model):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')

    def __str__(self):
        return self.name

class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')
    order_date = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа')
    is_completed = models.BooleanField(default=False, verbose_name='Завершен')

    def __str__(self):
        return f"Заказ №{self.pk} от {self.user}"

    def get_total_price(self):
        return sum([item.get_total_price() for item in self.order_items.all()])

class OrderedItem(models.Model):
    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name='Заказ')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, verbose_name='Позиция меню')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.menu_item.name} - {self.quantity}"

    def get_total_price(self):
        return self.menu_item.price * self.quantity


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(blank=True, null=True, verbose_name='О себе')
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True,
                                        verbose_name='Фотография профиля')

    def __str__(self):
        return self.user.username


class Promotion(models.Model):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')
    title = models.CharField(max_length=255, verbose_name='Название акции')
    description = models.TextField(verbose_name='Описание акции')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')

    def __str__(self):
        return self.title


class Event(models.Model):
    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    food_space = models.ForeignKey(FoodSpace, on_delete=models.CASCADE, verbose_name='Место питания')
    title = models.CharField(max_length=255, verbose_name='Название мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    start_date = models.DateTimeField(verbose_name='Дата и время начала')
    end_date = models.DateTimeField(verbose_name='Дата и время окончания')

    def __str__(self):
        return self.title
