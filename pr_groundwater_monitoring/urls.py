from django.contrib import admin
from django.urls import path
from app_monitor.views.vw_sensordata import sensor_data
from app_monitor.views.vw_dashboard import index
from app_monitor.views.vw_borehole import borehole_add, borehole_success, borehole_list, borehole_list_data

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home/Dashboard
    path('', index, name='index'),

    # Sensor Data
    path('data/', sensor_data, name='sensor_data'),

    # Borehole
    path('borehole_add/', borehole_add, name='borehole_add'),
    path('borehole_success/', borehole_success, name='borehole_success'),
    path('borehole_list/', borehole_list, name='borehole_list'),  # New URL for borehole list
     path('borehole_list_data/', borehole_list_data, name='borehole_list_data'),  # URL for HTML data

]
