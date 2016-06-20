from dateutil.parser import parse
from models import Type, Room, Sensor, Detection


def detection_by_timestamp(last_timestamp=""):
        detection_list = []
        dateTimes = Detection.objects.values('timestamp').distinct()
        if last_timestamp.__len__() != 0:
            last_timestamp = parse(last_timestamp, dayfirst=True)
            dateTimes = dateTimes.filter(timestamp__gt=last_timestamp)

        for time in dateTimes:
            detections = Detection.objects.values('timestamp', 'value', 'sensor_id').filter(timestamp=time['timestamp'])
            rooms = Room.objects.values('name', 'id')
            roomList = []

            for room in rooms:
                sensors_in_room = Sensor.objects.values('id', 'type_id').filter(room_id=room['id'])
                sensors = detections.filter(sensor_id=sensors_in_room.values('id'))
                sensorsList = []

                for sensor in sensors:
                    current_sensor = Sensor.objects.values('id', 'room_id', 'type_id').filter(id=sensor['sensor_id'])
                    s_type = Type.objects.values('type', 'valMax', 'valMin').filter(id=current_sensor.values('type_id'))
                    value = detections.values('value').filter(sensor_id=sensor['sensor_id'])
                    sensor_dict = {"id": sensor['sensor_id'],
                                   "type": s_type.values('type').get()['type'],
                                   "value": value.get()['value'],
                                   "valMax": s_type.get()['valMax'],
                                   "valMin": s_type.get()['valMin']
                                   }

                    sensorsList.append(sensor_dict)
                if sensorsList.__len__() != 0:
                    room_dict = {"name": room['name'],
                                 "sensors": sensorsList
                                 }
                    roomList.append(room_dict)

            detection_dict = {"detections": {"timestamp": time['timestamp'],
                                             "rooms": roomList
                                             }}

            detection_list.append(detection_dict)
        return detection_list
