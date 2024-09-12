from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'department']

    new_department = forms.CharField(max_length=100, required=False)