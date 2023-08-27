from django.urls import path
from . import views

urlpatterns = [
   # path('',views.homepage,name='homepage'),
    path('register/', views.register_request, name='register'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('predictions/', views.display_predictions, name='display_predictions'),
    path(r'form', views.my_form, name='form')
]