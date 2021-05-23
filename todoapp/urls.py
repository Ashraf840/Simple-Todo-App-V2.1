from django.urls import path
from . import views

urlpatterns = [
    path('', views.allTodos, name='alltodos'),
    path('delete_task/<int:pk>', views.deleteTodos, name='deletetodos'),
    path('edit_task/<int:pk>', views.editTodos, name='edittodos'),
]