from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('save_user/', views.save_user , name='save_user'),
    path('all_users/', views.get_users, name='get_users'),
    path('validate_user/', views.validate_user, name='validate_user')
]