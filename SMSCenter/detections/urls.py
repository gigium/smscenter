from django.conf.urls import url
from detections import views

urlpatterns = [
    url(r'^detections/$', views.DetectionList.as_view()),
]
