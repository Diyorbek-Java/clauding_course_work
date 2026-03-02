from rest_framework import viewsets
from app.models.department import Department
from app.serializers.department import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer