# core/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views  # ← добавь эту строку
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/add/', views.CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/edit/', views.CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
