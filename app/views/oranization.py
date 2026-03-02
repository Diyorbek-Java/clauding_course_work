from rest_framework import viewsets
from app.models.organization import Organization
from app.serializers.organization import OrganizationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing orgnization.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    