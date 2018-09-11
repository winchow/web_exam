from rest_framework import viewsets
from exam.serializers import LacSerializer,SubjectSerializer
from exam.models import Lac,Subject

class LacViewSet(viewsets.ModelViewSet):
    queryset = Lac.objects.all()
    serializer_class = LacSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


