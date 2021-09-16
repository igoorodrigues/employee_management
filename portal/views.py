from django.shortcuts import render

from portal.models import Employee


def employee(request):
    employees = Employee.objects.all()

    context = {
        'employess': employees
    }

    return render(request, 'portal/employee.html', context=context)
