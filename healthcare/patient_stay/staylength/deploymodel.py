import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained XGBoost model
model = joblib.load('model.joblib')

# Example values from the first row
data = {
    'Hospital_code': [14.0],
    'Hospital_type_code': [0.0],
    'City_Code_Hospital': [1.0],
    'Available Extra Rooms in Hospital': [2.0],
    'Department': [1.0],
    'Ward_Type': [3.0],
    'Bed Grade': [2.0],
    'City_Code_Patient': [8.0],
    'Type of Admission': [1.0],
    'Severity of Illness': [2.0],
    'Visitors with Patient': [2.0],
    'Age': [2.0],
    'Admission_Deposit': [5239.0],
    'count_id_patient': [5.0],
    'count_id_patient_hospitalCode': [1.0],
    'count_id_patient_wardfacilityCode': [1.0]
}

# Create a DataFrame from the dictionary
test_data = pd.DataFrame(data)

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
