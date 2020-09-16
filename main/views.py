from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    logged_in = is_logged_in(request)
    context = {'user': None}
    if logged_in:
        context['user'] = request.session['user']
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html', context)

def is_logged_in(request):
    try:
        if request.session['user']:
            return True
    except KeyError:
        return False