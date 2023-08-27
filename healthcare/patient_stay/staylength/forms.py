from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patientinfo


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class MyForm(forms.ModelForm):
  class Meta:
    model = Patientinfo
    fields = ['fullname','Hospital_code','Hospital_type_code','City_Code_Hospital','Available_Extra_Rooms_in_Hospital','Department','Ward_Type','Bed_Grade','City_Code_Patient','Type_of_Admission','Severity_of_Illness','Visitors_with_Patient','Age','Admission_Deposit','count_id_patient','count_id_patient_hospitalCode','count_id_patient_wardfacilityCode']
    labels = {'Name':"fullname",'Hospital Code':"Hospital_code",'Hospital Type Code':"Hospital_type_code",'City Code Hospital':"City_Code_Hospital",'Available Extra Rooms in Hospital':"Available_Extra_Rooms_in_Hospital",'Department':"Department",'Ward Type':"Ward_Type",'Bed Grade':"Bed_Grade",'City Code Patient':"City_Code_Patient",'Type of Admission':"Type_of_Admission",'Severity of Illness':"Severity_of_Illness",'Visitors with Patient':"Visitors_with_Patient",'Age':"Age",'Admission Deposit':"Admission_Deposit",'Count id Patient':"count_id_patient",'Count Id Patient HospitalCode':"count_id_patient_hospitalCode",'Count Id Patient WardfacilityCode':"count_id_patient_wardfacilityCode"}