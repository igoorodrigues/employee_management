from django.shortcuts import render, redirect

from portal.forms import EmployeeForm
from portal.models import Employee


def home(request):
    return render(request, 'portal/home.html')


def employee(request):
    employees = Employee.objects.all()

    busca = request.GET.get('search')
    if busca:
        employees = employees.filter(nome__icontains=busca)

    return render(request, 'portal/employee.html', {'employees': employees})


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


def employee_edit(request, employee_pk):
    employee = Employee.objects.get(pk=employee_pk)

    form = EmployeeForm(request.POST or None, instance=employee)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('employee')

    context = {
        'form': form,
        'employee': employee
    }

    return render(request, 'portal/employee_edit.html', context=context)


def employee_delete(request, employee_pk):
    employee = Employee.objects.get(pk=employee_pk)
    employee.delete()

    return redirect('employee')
