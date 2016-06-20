from __future__ import unicode_literals

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Room name : " + self.name


class Type(models.Model):
    valMin = models.FloatField(null=True)
    valMax = models.FloatField(null=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)


class Sensor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    room_id = models.ForeignKey(Room, models.CASCADE)
    type_id = models.ForeignKey(Type, models.CASCADE)

    def __str__(self):
        return " sensor ID : " + str(self.id)


class Detection(models.Model):
    value = models.FloatField(null=True)
    timestamp = models.DateTimeField()

    @property
    def lifespan(self):
        return '%s - present' % self.timestamp.strftime('%d/%m/%Y %H:%M:%S')

    sensor_id = models.ForeignKey(Sensor, models.DO_NOTHING)
