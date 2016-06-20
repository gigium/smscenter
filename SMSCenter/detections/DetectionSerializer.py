from rest_framework import serializers


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField(max_length=100)
    value = serializers.FloatField()
    valMax = serializers.FloatField()
    valMin = serializers.FloatField()


class RoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    sensors = SensorSerializer(many=True, required=False)


class DetectionSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField("%d/%m/%Y/ %H:%M:%S")
    rooms = RoomSerializer(many=True)


class Serializer(serializers.Serializer):
    detections = DetectionSerializer()
