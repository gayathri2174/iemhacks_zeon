from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Patient

def staylength(request):
    mypatient = Patient.objects.all().values()
    template=loader.get_template('display_patient.html')
    context={
        'mypatient': mypatient,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
