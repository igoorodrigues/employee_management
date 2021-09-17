from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.employee, name='employee'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:employee_pk>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:employee_pk>/', views.employee_delete, name='employee_delete')
]
