from django.shortcuts import render
from users.models import Users
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def save_user(request):
    user = Users()
    user.fname = request.GET['fname']
    user.lname = request.GET['lname']
    user.email = request.GET['email']
    user.password = request.GET['password']
    user.save()
    msg = "<h1>Saved Successfully</h1>"
    return HttpResponse(msg)

def validate_user(request):
    user = Users.objects.filter(email=request.GET['email'],password=request.GET['password'])
    
    if user:
        msg = "<h1>Login Successfull</h1>"
        return HttpResponse(msg)
    else:
        msg = "<h1>Login Unsuccessfull</h1>"
        return HttpResponse(msg)

def get_users(request):
    users = Users.objects.all()    
    context = {
        'users': users
    }
    return render(request, 'users/users.html', context)
        