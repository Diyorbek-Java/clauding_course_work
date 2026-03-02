from rest_framework import viewsets
from app.models.job_position import JobPosition
from app.serializers.job_position import JobPositionSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


class JobPositionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing job position.
    """
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    