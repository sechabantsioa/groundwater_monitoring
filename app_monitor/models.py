from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column="user_id")
    username = models.CharField(max_length=150, unique=True, db_column="username")
    email = models.EmailField(max_length=255, unique=True, db_column="email")
    phone_number = models.CharField(max_length=20, db_column="phone_number")

    class Meta:
        managed = True
        db_table = 'User'

    def __str__(self):
        return self.username

class Borehole(models.Model):
    borehole_id = models.AutoField(primary_key=True, db_column="borehole_id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id", null=True, blank=True)
    location = models.CharField(max_length=255, db_column="location")
    depth = models.DecimalField(max_digits=10, decimal_places=2, db_column="depth")
    diameter = models.DecimalField(max_digits=5, decimal_places=2, db_column="diameter")
    sensor_id = models.CharField(max_length=50, db_column="sensor_id")

    class Meta:
        managed = True
        db_table = 'Borehole'

    def __str__(self):
        return f"Borehole {self.borehole_id} at {self.location}"

class SensorData(models.Model):
    sensor_id = models.CharField(max_length=50, primary_key=True, db_column="sensor_id") #Should be primary key.
    borehole = models.ForeignKey(Borehole, on_delete=models.CASCADE, db_column="borehole_id")
    timestamp = models.DateTimeField(auto_now_add=True, db_column="timestamp")
    water_level = models.DecimalField(max_digits=5, decimal_places=2, db_column="water_level")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, db_column="temperature")
    pressure = models.DecimalField(max_digits=5, decimal_places=2, db_column="pressure")
    water_quality = models.CharField(max_length=100, db_column="water_quality")

    class Meta:
        managed = True
        db_table = 'SensorData'

    def __str__(self):
        return f"SensorData {self.sensor_id} at {self.timestamp}"
