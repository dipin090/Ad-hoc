from rest_framework import serializers
from my_project.models import hospital_department, paitents


class paitentsserializer(serializers.ModelSerializer):
    class Meta:
        model = paitents
        fields = "__all__"


class hospital_departmentserializer(serializers.ModelSerializer):
    task = paitentsserializer(read_only=True, many=True)

    class Meta:
        model = hospital_department
        fields = "__all__"
