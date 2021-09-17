from django.shortcuts import render, redirect

from portal.models import Employee
from portal.forms import EmployeeForm


def home(request):
    return render(request, 'portal/home.html')


def employee(request):
    employees = Employee.objects.all()

    context = {
        'employess': employees
    }

    return render(request, 'portal/employee.html', context=context)


def employee_add(request):
    form = EmployeeForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('employee')

    context = {
        'form': form
    }

    return render(request, 'portal/employee_add.html', context=context)
