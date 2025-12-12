from django.urls import path
from . views import *
from accounts import views as Accountsviews
urlpatterns = [
    path('profile/',profile,name='profile'),
    path('',Accountsviews.vendordashboard , name='vendor'),
    path('menu-builder/',menu_builder,name='menu_builder'),

    # Category urls
    path('menu-builder/category/<int:pk>/',food_by_category,name='food_by_category'),
    path('menu-builder/category/add/',add_category,name='add_category'),
    path('menu-builder/category/edit/<int:pk>/',edit_category,name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/',delete_category,name='delete_category'),

    ## Food urls 
    path('menu-builder/food/',add_food,name='add_food'),
    path('menu-builder/food/edit/<int:pk>/',edit_food,name='edit_food'),
    path('menu-builder/food/delete/<int:pk>/',delete_food,name='delete_food'),
]
 