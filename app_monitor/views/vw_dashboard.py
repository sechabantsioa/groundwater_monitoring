from django.shortcuts import render
from app_monitor.models import Borehole, SensorData
from app_monitor.utils import generate_random_sensor_data


def index(request):
    generate_random_sensor_data()  # Generate random data

    boreholes = Borehole.objects.all()
    sensor_data = SensorData.objects.all().order_by('-timestamp')[:len(boreholes)]  # Fetch recent data for each borehole

    context = {
        'boreholes': boreholes,
        'sensor_data': sensor_data
    }
    return render(request, 'home/index.html', context)
