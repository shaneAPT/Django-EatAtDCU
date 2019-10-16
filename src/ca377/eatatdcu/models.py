from django.db import models
import datetime

class Campus(models.Model):
   campus_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Restaurant(models.Model):
   restaurant_id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   location = models.CharField(max_length=100)
   campus_id = models.ForeignKey(Campus,on_delete = models.CASCADE)
   opening_hours = models.TimeField()
   closing_hours = models.TimeField()
   capacity = models.IntegerField()
   is_staff_only = models.BooleanField(default=False)
   is_restaurant = models.BooleanField(default=False)
   is_open_wknd = models.BooleanField(default=False)
   opening_hours_wknd = models.TimeField(default=datetime.time(00, 00))
   closing_hours_wknd = models.TimeField(default=datetime.time(00, 00))
   map_location = models.CharField(max_length=200)

   def __str__(self):
      return self.name

