from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    path = request.path
    method = request.method
    content = """
    <center><h2>Testing Django Request Response Objects</h2>
    <p>Request path : " {}</p>
    <p>Request Method : {}</p></center>
    """.format(
        path, method
    )
    return HttpResponse(content)


def pathview(request, name, id):
    return HttpResponse(f"Name:{name} UserID:{id}")


def home(request):
    return HttpResponse("Hello- this is the home page!")
