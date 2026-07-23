from django.shortcuts import render, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all().order_by("-joined_date")
    return render(request, "staff/list.html", {"employees": employees})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "staff/detail.html", {"employee": employee})


def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff:list")
    else:
        form = EmployeeForm()
    return render(request, "staff/employee_form.html", {"form": form})

def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('staff:list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'staff/employee_form.html', {'form': form})


def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('staff:list')
    return render(request, 'staff/employee_confirm_delete.html', {'employee': employee})
