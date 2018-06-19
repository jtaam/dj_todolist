from rest_framework import serializers
from .models import ToDoElements


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoElements
        fields = 'id', 'todo_text', 'todo_done'
