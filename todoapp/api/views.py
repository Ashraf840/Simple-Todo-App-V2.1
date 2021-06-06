from todoapp.models import MyTodo

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from .serializers import MyTodoSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


######## Function Based api_view()

# APIs are tested using POSTMAN


# Overview of API Endpoints
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detail View': 'task-detail/<str:pk>',
        'Create': 'task-create/',
        'Update': 'task-update/<str:pk>',
        'Delete': 'task-delete/<str:pk>',
    }
    return Response(api_urls)


# List out all the tasks
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
def taskList(request):
    tasks = MyTodo.objects.order_by('-id')
    serializer = MyTodoSerializer(tasks, many = True)
    return Response(serializer.data)


# Detail view of a specific tasks
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
def taskDetail(request, pk):
    task = MyTodo.objects.get(id=pk)
    serializer = MyTodoSerializer(task)
    return Response(serializer.data)


# Create new tasks
@api_view(['POST'])
def taskCreate(request):
    serializer = MyTodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        #after creation, return the new task-list
        tasks = MyTodo.objects.order_by('-id')
        serializer = MyTodoSerializer(tasks, many = True)
    return Response(serializer.data)


# Update a specific task
@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
def taskUpdate(request, pk):
    task = MyTodo.objects.get(id=pk)
    serializer = MyTodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Delete a specific task
@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
def taskDelete(request, pk):
    task = MyTodo.objects.get(id=pk)
    task.delete()

    #after deletion, return the new task-list
    tasks = MyTodo.objects.order_by('-id')
    serializer = MyTodoSerializer(tasks, many = True)
    return Response(serializer.data)
