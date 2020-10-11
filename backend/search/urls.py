from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.FoodAPIView.as_view()),
]