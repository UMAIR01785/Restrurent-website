from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Myaccounts),
    path('registerUser/',registeruser,name='registeruser'),
    path('registervendor/',registervendor,name='registervendor'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cusdashboard/',cusdashboard,name='cusdashboard'),
    path('vendordashboard/',vendordashboard,name='vendordashboard'),
    path('Myaccounts/',Myaccounts,name='Myaccounts'),
    path('activate<uid64>/<token>/',activate,name='activate'),
    path('forgot/',forgot,name='forgot'),
    path('reset_password<uid64>/<token>/',reset_password,name='reset-password'),
    path('reset/',reset,name='reset'),
    path('vendor/',include('vendor.urls')),
]
