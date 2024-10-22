from django.db import models

class Schedule(models.Model):
    schedule_file = models.FileField(upload_to='schedules/')
    processed_file = models.FileField(upload_to='processed_schedules/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    equipment_name = models.CharField(max_length=255)
    phase = models.CharField(max_length=50)
    priority = models.IntegerField()
