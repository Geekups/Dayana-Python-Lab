from rest_framework import serializers
from .models import toDo

class toDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDo # my model name
        fields = ('id', 'Title', 'Description', 'Date', 'Completed') # give it the filds we want
        