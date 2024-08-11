from django.urls import path
from .views import *

urlpatterns =[
    path("", add_view, name="addview"),
    path("update//<int:id>", update_student, name="update"),
    path("delete//<int:id>", delete, name="delete"),
]