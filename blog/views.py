from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """<html>
        <head></head>
        <body>
        <ul>
            <li><a href="accounts/login">Login</a></li>
            <li><a href="accounts/register">Signup</a></li>   
            <li><a href="accounts/all_users">All users</a></li>         
        </ul>
        </body>
    </html>"""
    return HttpResponse(html)