from rest_framework import viewsets
from app.models.department import Department
from app.serializers.department import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

     
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    