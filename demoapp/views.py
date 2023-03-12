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


def qryview(request):
    get = request.GET
    return HttpResponse(f"Name:{get['name']} UserID:{get['id']}")


def showform(request):
    return render(request, "form.html")


def getform(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse(f"Name:{name} UserID:{id}")


def menuitems(request, dish):
    items = {
        "pasta": "Pasta is a type of noodle blah blah",
        "falafel": "Falafel are deep fried patties or balls made from blah blah",
        "cheesecake": "Cheesecake is a type of dessert made with blah blah",
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>{description}")
