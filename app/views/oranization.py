from rest_framework import viewsets
from app.models.organization import Organization
from app.serializers.organization import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing orgnization.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer