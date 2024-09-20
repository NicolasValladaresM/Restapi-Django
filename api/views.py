from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ProgrammerSerializer, AnimalSerializer
from .models import Programmer, Animal
from rest_framework.decorators import action


class ProgramerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        count = queryset.count()
        serializer= self.get_serializer(queryset, many=True)
        return Response({'count': count, 'data': serializer.data})
    
    @action(detail=False, methods=['get'])
    def filterbyAge(self, request):
        filteredQuery = self.queryset.filter(age__gt=18)
        serializer = self.get_serializer(filteredQuery, many=True)
        return Response({'count': filteredQuery.count(), 'data': serializer.data})

class AnimalViewSet(viewsets.ModelViewSet):
    queryset= Animal.objects.all()
    serializer_class = AnimalSerializer
    
    @action(detail=False, methods=['get'])
    def filterByActives(self, request):
        activesQuery =  self.queryset.filter(vertebled=True)
        serializer = self.get_serializer(activesQuery, many=True)
        return Response({'count': activesQuery.count(), 'data': serializer.data})

# Create your views here.
