from django.db import models



class Patientinfo(models.Model):
  fullname = models.CharField(max_length=200)
  Hospital_code = models.IntegerField()
  Hospital_type_code =  models.CharField(max_length=200)
  City_Code_Hospital= models.IntegerField()
  Available_Extra_Rooms_in_Hospital= models.IntegerField()
  Department= models.CharField(max_length=200)
  Ward_Type= models.CharField(max_length=200)
  Bed_Grade= models.IntegerField()
  City_Code_Patient= models.IntegerField()
  Type_of_Admission=models.CharField(max_length=200)
  Severity_of_Illness = models.CharField(max_length=200)
  Visitors_with_Patient =models.IntegerField()
  Age = models.IntegerField()
  Admission_Deposit =models.IntegerField()
  count_id_patient = models.IntegerField()
  count_id_patient_hospitalCode =models.IntegerField()
  count_id_patient_wardfacilityCode = models.IntegerField()
