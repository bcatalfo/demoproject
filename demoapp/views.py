from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm


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


def secretmessage(request):
    if request.user.is_anonymous:
        raise PermissionDenied()
    return HttpResponse("Steven likes Pokemon :3")


@login_required
def secretmessage2(request):
    return HttpResponse("Dan likes Kirby ^-^")


def qryview(request):
    get = request.GET
    return HttpResponse(f"Name:{get['name']} UserID:{get['id']}")


def showclassform(request):
    form = ApplicationForm()

    return render(request, "classform.html", {"f": form})


def getclassform(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    form = ApplicationForm(request.POST)
    if not form.is_valid():
        return HttpResponseForbidden("Invalid form")
    name = form.cleaned_data["name"]
    field = form.cleaned_data["field"]
    return HttpResponse(
        f"Congratulations, {name}! You have successfully submitted your application for {field}."
    )


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
