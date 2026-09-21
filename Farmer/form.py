from .models import Farmers
from django import forms

class Farmerform(forms.ModelForm):
    class Meta:
        model = Farmers
        fields = ['name', 'phone', 'village', 'taluka', 'district','problem']
        labels = {'name':'Enter Name','phone':'Enter Phone_no','village':'Enter village','taluka':'Enter Taluka','district':'Enter District','problem':'Enter Problem'}
