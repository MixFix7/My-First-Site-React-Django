from .models import UkraineAlarmsStatus
from rest_framework import viewsets, permissions
from .serializers import UkraineSerializer
from .ukraine_alarms import get_alarms
from .api_key import get_apikey


class UkraineViewSet(viewsets.ModelViewSet):
    queryset = UkraineAlarmsStatus
    get_alarms()
    get_apikey()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UkraineSerializer


