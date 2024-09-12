from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            new_department_name = form.cleaned_data.get('new_department')
            if new_department_name:
                department, _ = Department.objects.get_or_create(name=new_department_name)
                employee.department = department
            employee.save()
            return redirect('emp_list')  # Make sure this name matches your URL pattern
    else:
        form = EmployeeForm()
    
    departments = Department.objects.all()
    return render(request, 'add_emp.html', {'form': form, 'departments': departments})

def delete_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_list')
    
    return render(request, 'delete_emp.html', {'employee': employee})

def update_emp(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'update_emp.html', {'form': form, 'employee':employee})
