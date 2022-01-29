from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import CarSerializer
from .models import Car
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# Create your views here.
class CarCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarView(generics.ListAPIView):       
    permission_classes = (IsAuthenticated, IsOwner) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Car.objects.all()
    serializer_class = CarSerializer