from django.urls import path
from . import views

app_name = 'userAuthApp'

urlpatterns = [
    path('user_registration/', views.userRegistration, name='user_reg'),
    path('user_login/', views.userLogin, name='user_login'),
    path('user_logout/', views.userLogout, name='user_logout'),
]