from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('appointments/', include('appointments.urls')),
    path('', lambda _: redirect('appointment_list'))
]
