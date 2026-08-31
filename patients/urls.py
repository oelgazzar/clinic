from django.urls import path

from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('new/', views.new_patient, name='new_patient'),
    path('<int:patient_id>/', views.patient_details, name='patient_details'),
    path('<int:patient_id>/edit/', views.edit_patient, name='edit_patient'),
    path('<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),
]