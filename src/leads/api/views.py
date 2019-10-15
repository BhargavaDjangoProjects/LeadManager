from rest_framework import viewsets, permissions
from .serializers import LeadSerializer
from leads.models import Lead


class LeadViewset(viewsets.ModelViewSet):
    permission_classes = [
      permissions.IsAuthenticated
    ]
    serializer_class = LeadSerializer

    def get_queryset(self, *args, **kwargs):
        return self.request.user.leads.all()
