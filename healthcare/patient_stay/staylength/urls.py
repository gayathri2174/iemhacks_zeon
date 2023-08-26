from django.urls import path
from . import views

urlpatterns = [
    path('staylength/', views.staylength, name='staylength'),
]