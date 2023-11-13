from django.db import models


class Model(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Model, on_delete=models.PROTECT)
    model = models.CharField(max_length=100, blank=True, null=True)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField( blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
      return self.model
    

class CarInventory(models.Model):
   cars_count = models.IntegerField()
   cars_value = models.FloatField()
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['-created_at']

   def __str__(self):
      return f'{self.cars_count} - {self.cars_value}'