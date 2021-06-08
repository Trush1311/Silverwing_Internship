from django.urls import path
from.views import hello

urlpattern = [
    path('hello/',hello),
]