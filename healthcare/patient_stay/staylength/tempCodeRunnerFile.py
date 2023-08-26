import pandas as pd

# Sample test data
test_data = pd.DataFrame({
    'Hospital_code': [8],
    'Hospital_type_code': ['c'],
    'City_Code_Hospital': [3],
    'Hospital_region_code': ['X'],
    'Available Extra Rooms in Hospital': [3],
    'Department': ['radiotherapy'],
    'Ward_Type': ['R'],
    'Ward_Facility_Code': ['D'],
    'Bed Grade': [2],
    'patientid': [7],
    'City_Code_Patient': [8],
    'Type of Admission': ['Emergency'],
    'Severity of Illness': ['Extreme'],
    'Visitors with Patient': [2],
    'Age': ['51-60'],
    'Admission_Deposit': [4911]
})

# Convert categorical columns to numerical using Label Encoding
categorical_cols = ['Hospital_type_code', 'Hospital_region_code', 'Department', 'Ward_Type', 'Ward_Facility_Code',
                    'Type of Admission', 'Severity of Illness', 'Age']

for col in categorical_cols:
    le = LabelEncoder()
    test_data[col] = le.fit_transform(test_data[col])

# Load the trained model
reg = joblib.load('model.joblib')

# Make predictions
predictions = reg.predict(test_data)

# Print the predictions
print("Predicted Stay:", predictions)
