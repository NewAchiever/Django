from django.shortcuts import render, redirect
from users.models import Users
from django.http import HttpResponse


# Create your views here.
def login(request):
    if len(request.GET) == 0:
        return render(request, 'users/login.html')
    else:
        user = Users.objects.filter(email=request.GET['email'],password=request.GET['password'])

        if len(user) != 0:
            user = user[0]
        else:
            context = {
                'invalid_cred':'Invalid Credentials.Try again.'
            }
            return render(request, 'users/login.html', context)
        
        if user:
            request.session['user'] = user.fname
            return redirect('home')
        else:
            return redirect('home')

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('home')

def signup(request):
    if len(request.GET) == 0:
        return render(request, 'users/signup.html')
    else:
        user = Users()
        user.fname = request.GET['fname']
        user.lname = request.GET['lname']
        user.email = request.GET['email']
        user.password = request.GET['password']
        user.save()
        request.session['user'] = user.fname
        return redirect('home')
    

def get_users(request):
    users = Users.objects.all()    
    context = {
        'users': users
    }
    return render(request, 'users/users.html', context)
        