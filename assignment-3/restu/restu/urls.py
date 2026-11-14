from django.contrib import admin
from django.urls import path, include

from meal.views import meal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meal.urls')),
    path('show_meals/', meal, name='meal'),
    path('about_us/', include('about_us.urls')),
]
