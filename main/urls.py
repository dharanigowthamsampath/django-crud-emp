from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name='emp_list'),
    path('add/', views.add_employee, name='add_emp'),
    path('delete/<int:pk>', views.delete_emp, name='delete_emp'),
    path('update/<int:pk>', views.update_emp, name='update_emp')
]