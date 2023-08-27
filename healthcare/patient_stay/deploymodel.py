import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_stay.settings")

django.setup()
from staylength.models import Patientinfo  # Replace 'your_app' with the actual app name

# Load the trained XGBoost model
model = joblib.load('model.joblib')

# Fetch data from the database
patient_info_instances = Patientinfo.objects.all()
for instance in patient_info_instances:
    print("Hospital_code:", instance.Hospital_code)
    print("Hospital_type_code:", instance.Hospital_type_code)
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

# Print the predictions
print("Predicted Stay:", predictions)
