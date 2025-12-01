from django.urls import path
from .views import *

urlpatterns = [
    path('registerUser/',registeruser,name='registeruser'),
    path('registervendor/',registervendor,name='registervendor'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('cusdashboard/',cusdashboard,name='cusdashboard'),
    path('vendordashboard/',vendordashboard,name='vendordashboard'),
    path('Myaccounts/',Myaccounts,name='Myaccounts'),
    path('activate<uid64>/<token>/',activate,name='activate')
]
