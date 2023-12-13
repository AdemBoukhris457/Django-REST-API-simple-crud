from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class AllCarsListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    partial = True
    
    
class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Car"))