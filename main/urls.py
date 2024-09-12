from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name='emp_list'),
    path('add/', views.add_employee, name='add_emp')
]