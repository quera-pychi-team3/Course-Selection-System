from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from accounts.filters.educational_deputy import EducationalDeputyFilter
from accounts.models.educational_deputy import EducationalDeputy
from accounts.serializers.educational_deputy import EducationalDeputySerializer

class EducationalDeputyViewSet(ModelViewSet):
    queryset = EducationalDeputy.objects.all()
    serializer_class = EducationalDeputySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EducationalDeputyFilter
