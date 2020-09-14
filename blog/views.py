from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """<html>
        <head></head>
        <body>
        <ul>
            <li><a href="/posts">posts</a></li>
            
        </ul>
        </body>
    </html>"""
    return HttpResponse(html)