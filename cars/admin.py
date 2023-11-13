from django.contrib import admin
from cars.models import *


class ModelAdmin(admin.ModelAdmin):
  search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
  list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'plate', 'image', 'description')
  search_fields = ('model', 'brand')



admin.site.register(Model, ModelAdmin)
admin.site.register(Car, CarAdmin)





