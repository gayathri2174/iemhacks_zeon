# views.py
from django.shortcuts import render, redirect
from .models import Patientinfo
from .forms import MyForm , NewUserForm
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout #add this



def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'patientstay.html', {'form': form})

def home(request):
  return render(request, 'homepage.html')
    

def display_predictions(request):
    # Load the trained XGBoost model
    model = joblib.load('model.joblib')
    
    # Fetch data from the database
    patient_info_instances = Patientinfo.objects.all()

    # Create a list of dictionaries to hold the data
    data_list = []
    for instance in patient_info_instances:
        data_list.append({
            'Hospital_code': instance.Hospital_code,
            'Hospital_type_code': instance.Hospital_type_code,
            'City_Code_Hospital': instance.City_Code_Hospital,
            'Available Extra Rooms in Hospital': instance.Available_Extra_Rooms_in_Hospital,
            'Department': instance.Department,
            'Ward_Type': instance.Ward_Type,
            'Bed Grade': instance.Bed_Grade,
            'City_Code_Patient': instance.City_Code_Patient,
            'Type of Admission': instance.Type_of_Admission,
            'Severity of Illness': instance.Severity_of_Illness,
            'Visitors with Patient': instance.Visitors_with_Patient,
            'Age': instance.Age,
            'Admission_Deposit': instance.Admission_Deposit,
            'count_id_patient': instance.count_id_patient,
            'count_id_patient_hospitalCode': instance.count_id_patient_hospitalCode,
            'count_id_patient_wardfacilityCode': instance.count_id_patient_wardfacilityCode
        })

    # Create a DataFrame from the list of dictionaries
    test_data = pd.DataFrame(data_list)

    # Convert categorical columns to numerical using Label Encoding
    categorical_cols = ['Hospital_type_code', 'Department', 'Ward_Type', 
                    'Type of Admission', 'Severity of Illness', 'Age']

    for col in categorical_cols:
        le = LabelEncoder()
        test_data[col] = le.fit_transform(test_data[col])

    # Make predictions
    predictions = model.predict(test_data)

    # Create a list to hold the predicted values
    predictions_list = predictions.tolist()

    # Render the template with the predicted values
    context = {'predictions': predictions_list}
    return render(request, 'display_patient.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")