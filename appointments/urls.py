from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('new/', views.new_appointment, name='new_appointment'),
    path('<int:appointment_id>/', views.appointment_details, name='appointment_details'),
    path('<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
]