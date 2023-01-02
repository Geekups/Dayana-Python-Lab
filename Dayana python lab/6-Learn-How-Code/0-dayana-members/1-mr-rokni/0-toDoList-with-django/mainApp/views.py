from django.shortcuts import render
from rest_framework import generics
from .serializers import toDoSerializer
from .models import toDo


class ListCreateToDo(generics.ListCreateAPIView):               #Read & Create
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer

class UpdateDeleteToDo(generics.RetrieveUpdateDestroyAPIView):   #Update & Delete
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer
