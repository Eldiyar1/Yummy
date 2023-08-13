from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('food_spaces/', include('apps.food_space.urls'))
]
