from django.contrib import admin
from .models import User, Borehole, SensorData

# Register your models here.
admin.site.register(User)
admin.site.register(Borehole)
admin.site.register(SensorData)