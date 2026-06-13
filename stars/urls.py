from django.urls import path
from .views import *

app_name = "stars"

urlpatterns = [
    path('new-star/', new_star, name='new_star'), 
    path('create/', create, name='create'),
]