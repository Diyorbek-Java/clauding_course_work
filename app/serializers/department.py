# app/serializers/department.py
from rest_framework import serializers
from app.models.department import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'