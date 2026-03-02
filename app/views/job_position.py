from rest_framework import viewsets
from app.models.job_position import JobPosition
from app.serializers.job_position import JobPositionSerializer

class JobPositionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing job position.
    """
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer