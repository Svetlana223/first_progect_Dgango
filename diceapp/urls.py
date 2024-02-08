from django.urls import path
from . import views

urlpatterns = [
    path('coin/', views.coin, name="coin"),
    path('dice/', views.dice, name="dice"),
    path('rand_hundred/', views.rand_hundred, name="rand_hundred"),
]