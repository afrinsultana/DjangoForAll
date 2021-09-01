from django import forms
from django.db.models import fields    
from studentapp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields=('name','email','dob','gender','phone')
        fields='__all__'


