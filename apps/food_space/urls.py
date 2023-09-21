from rest_framework.routers import DefaultRouter
from .views import FoodSpaceViewSet, ReviewViewSet, ReservationViewSet, OrderViewSet, PromotionViewSet, EventViewSet

router = DefaultRouter()
router.register('food_spaces', FoodSpaceViewSet)
router.register('reviews', ReviewViewSet)
router.register('reservations', ReservationViewSet)
router.register('orders', OrderViewSet)
router.register('promotions', PromotionViewSet)
router.register('events', EventViewSet)

urlpatterns = router.urls