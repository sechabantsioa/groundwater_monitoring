import random
from datetime import datetime
from app_monitor.models import SensorData, Borehole

def generate_random_sensor_data():
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
            water_quality=random.choice(['Good', 'Moderate', 'Poor']) #'Choice' made after analyzing data.
        )
        sensor_data_list.append(sensor_data)

    SensorData.objects.bulk_create(sensor_data_list)
