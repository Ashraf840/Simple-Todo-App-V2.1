from rest_framework import serializers
from todoapp.models import MyTodo


class MyTodoSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyTodo
        fields = [
            'id',
            'task',
        ]

# This serializer ("MyTodoSerializer") need to be called 
# inside the "todoapp/api/views.py" file.

"""
Objectives of Serializer:
    - Converts to JSON
    - Validation for data passed
"""