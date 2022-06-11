from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path("result/<str:category>", views.category_result_view, name="result"),
]