from django.urls import path
from . import views

urlpatterns = [
    path('predictions/', views.display_predictions, name='display_predictions'),
    path(r'form', views.my_form, name='form')
]