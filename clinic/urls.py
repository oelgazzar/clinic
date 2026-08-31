from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('appointments/', include('appointments.urls')),
    path('', lambda _: redirect('appointment_list')),
    path('dashboard/', views.dashboard, name='dashboard'),
]
