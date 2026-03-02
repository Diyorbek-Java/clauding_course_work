from rest_framework import serializers
from app.models.job_position import JobPosition

class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'