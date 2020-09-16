from django.urls import path, include
from . import views as main_views
from users import views as user_views

urlpatterns = [
    path('', main_views.index, name='home'),
    path('login/', user_views.login, name='login'),
    path('signup/', user_views.signup, name='signup'),
    path('logout/', user_views.logout, name='logout')    
]