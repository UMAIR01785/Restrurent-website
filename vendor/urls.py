from django.urls import path
from . views import *
from accounts import views as Accountsviews
urlpatterns = [
    path('profile/',profile,name='profile'),
    path('',Accountsviews.vendordashboard , name='vendor')
]
