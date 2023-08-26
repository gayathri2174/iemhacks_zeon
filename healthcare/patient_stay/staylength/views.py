from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Patientinfo
from .forms import MyForm


def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'patientstay.html', {'form': form})


# Create your views here.
