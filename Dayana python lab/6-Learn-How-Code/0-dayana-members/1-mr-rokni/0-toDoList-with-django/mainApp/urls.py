from django.urls import path
from .views import UpdateDeleteToDo, ListCreateToDo

urlpatterns = [
    path('<int:pk>', UpdateDeleteToDo.as_view()), # <int:pk> = object's id # .as_view() = because type my view is class base view
    path('', ListCreateToDo.as_view(), name='ListCreateToDo')
]