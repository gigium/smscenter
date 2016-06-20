from django.contrib import admin
from .models import *


class TypeModelAdmin(admin.ModelAdmin):
    list_display = ["type", "valMin", "valMax"]

    class Meta:
        model = Type


class DetectionModelAdmin(admin.ModelAdmin):
    list_filter = ["timestamp", "sensor_id"]
    list_display = ["timestamp", "sensor_id", "value"]

    class Meta:
        model = Detection


admin.site.register(Room)
admin.site.register(Sensor)
admin.site.register(Type, TypeModelAdmin)
admin.site.register(Detection, DetectionModelAdmin)


