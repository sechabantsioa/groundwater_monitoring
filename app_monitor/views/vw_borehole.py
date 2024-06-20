from django.shortcuts import render, redirect
from app_monitor.models import Borehole, SensorData

def borehole_add(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        depth = request.POST.get('depth')
        diameter = request.POST.get('diameter')
        sensor_id = request.POST.get('sensor_id')

        borehole = Borehole(
            location=location,
            depth=depth,
            diameter=diameter,
            sensor_id=sensor_id,
        )
        borehole.save()
        return redirect('borehole_success')  # Redirect to a success page

    return render(request, 'borehole_add.html')

def borehole_success(request):
    return render(request, 'borehole_success.html')

def borehole_list(request):
    sensor_data = SensorData.objects.all().order_by('-timestamp')
    return render(request, 'borehole_list.html', {'sensor_data': sensor_data})

#For updates in real time.
def borehole_list_data(request):
    sensor_data = SensorData.objects.all().order_by('-timestamp')
    return render(request, 'borehole_list_data.html', {'sensor_data': sensor_data})


