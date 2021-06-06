from django.urls import path
from . import views

app_name = 'todoApp'

urlpatterns = [
    path('', views.allTodos, name='alltodos'),  # Retrieve, Create
    path('edit_task/<int:pk>', views.editTodos, name='edittodos'),
    path('delete_task/<int:pk>', views.deleteTodos, name='deletetodos'),
]