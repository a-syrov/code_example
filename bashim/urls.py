from django.urls import path
from .views import bash, abyssbest

urlpatterns = [
    path('', bash, name='bash'),
    path('abyssbest/', abyssbest, name='abyssbest'),   
]