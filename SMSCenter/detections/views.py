from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from DetectionSerializer import Serializer
from DetectionGetter import detection_by_timestamp
from rest_framework.response import Response
from rest_framework.views import APIView


class DetectionList(APIView):
    def get(self, request):
        timestamp = ""
        if request.GET.get('timestamp'):
            timestamp = request.GET.get('timestamp')
        det = detection_by_timestamp(timestamp)
        serializer = Serializer(det, many=True)
        return Response(serializer.data)

    def put(self, request):
        timestamp = request.PUT.get('timestamp')
        detections = request.PUT.get('detections')



def home(request):
    return render(request, "home.html", {})


def index(request):
    return HttpResponseRedirect("/home")


