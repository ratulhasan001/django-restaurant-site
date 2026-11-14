from django.urls import path
from . import views

urlpatterns = [
    # The landing page is served at "/" and, for older links, at "/meal/index/".
    path('', views.index, name='home'),
    path('meal/index/', views.index, name='index'),
    path('meal/', views.meal),
    path('show_meals/<int:category_id>/', views.meal_detail, name='meal_detail'),
]
