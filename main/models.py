from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='employees', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.department.name if self.department else 'No Department'}"