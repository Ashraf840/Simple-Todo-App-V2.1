from django.urls import path, include
# from .views import TodoAppRUDview
# from .views import apiOverview
from . import views


app_name = 'todoApi'

urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('task-list/', views.taskList, name='task_list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task_detail'),
    path('task-create/', views.taskCreate, name='task_create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task_update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task_delete'),
]
