from .models import Farmer_training
from django import forms

class Farmer_registration(forms.ModelForm):
    class Meta:
        model = Farmer_training
        fields = ['name','age','contact_number','village','taluka','district','crop_detail']
        labels = {'name':'Enter Name','age':'Enter Age','contact_number':'Enter Contact Number','village':'Enter Village','taluka':'Enter taluka','district':'Enter District','crop_detail':'Enter Crop Detail'}

