from django.http import JsonResponse
import random
from datetime import datetime
from app_monitor.models import SensorData, Borehole

def sensor_data(request):
    data = {
        "sensor_id": "S123", #This needs to remain constant for one sensor
        "borehole": "Ntsioa Borehole", #This needs to remain constant for one sensor
        "timestamp": datetime.now().isoformat(),
        "water_level": round(random.uniform(5.0, 10.0), 2),
        "temperature": round(random.uniform(10.0, 30.0), 2),
        "pressure": round(random.uniform(1.0, 5.0), 2),
        "water_quality": round(random.uniform(50.0, 100.0), 2)
    }
    return JsonResponse(data)

#To get random updates in real time for all sensors activate/uncomment the below code,and update views. (Code from utils.py)
'''def generate_random_sensor_data():
    boreholes = Borehole.objects.all()
    sensor_data_list = []

    for borehole in boreholes:
        sensor_data = SensorData(
            sensor_id=f"{borehole.sensor_id}_{random.randint(1, 1000)}",
            borehole=borehole,
            timestamp=datetime.now(),
            water_level=random.uniform(0, 10),
            temperature=random.uniform(10, 30),
            pressure=random.uniform(1, 5),
            water_quality=random.choice(['Good', 'Moderate', 'Poor'])
        )
        sensor_data_list.append(sensor_data)

    SensorData.objects.bulk_create(sensor_data_list)'''
