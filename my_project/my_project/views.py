from my_project.models import hospital_department,paitents
from my_project.serializers import paitentsserializer,hospital_departmentserializer
from rest_framework import viewsets


class hospitalapi(viewsets.ModelViewSet):
    queryset=hospital_department.objects.all()
    serializer_class=hospital_departmentserializer

class paitentsapi(viewsets.ModelViewSet):
    queryset=paitents.objects.filter(status="pending")
    serializer_class=paitentsserializer