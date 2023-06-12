from django.shortcuts import render
from rest_framework.views import APIView
from .models import UkraineAlarmsStatus
from .serializers import UkraineSerializer
from rest_framework.response import Response


class UkraineAlarmsView(APIView):
    def get(self, request):
        alarms = UkraineAlarmsStatus.objects.all()
        serializer_alarms = UkraineSerializer(alarms, many=True)
        output = serializer_alarms.data
        return Response(output)



