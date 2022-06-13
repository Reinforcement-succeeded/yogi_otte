from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path("result/<str:category>", views.category_result_view, name="result"),
    path('result/mood/', views.mood_result_view, name='mood_result'),
    path('result/location/', views.location_result_view, name='location_result')
]