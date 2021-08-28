from django import forms
from django.db.models import fields    
from studentapp.models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        # fields=('name','email','dob','gender','phone')
        fields='__all__'


