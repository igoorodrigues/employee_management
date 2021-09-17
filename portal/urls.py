from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.employee, name='employee'),
    path('employee/add/', views.employee_add, name='employee_add'),

]
