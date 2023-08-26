from django.urls import path
from . import views

urlpatterns = [
    
    path(r'form', views.my_form, name='form')
]