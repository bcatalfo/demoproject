from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getuser/<name>/<int:id>", views.pathview, name="pathview"),
    path("getuser/", views.qryview, name="qryview"),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name="getform"),
    path("dishes/<str:dish>", views.menuitems),
    path("showclassform/", views.showclassform),
    path("getclassform/", views.getclassform),
    path("hello/", views.hello_template),
]
