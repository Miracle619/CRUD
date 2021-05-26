from django.shortcuts import redirect, render
from employee.forms import EmployeeForm
from employee.models import Employee
# Create your views here.

# This method is to save the employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


# This method is to Show all the Employee
def show(request):
    employess = Employee.objects.all()
    return render(request, 'show.html', {'employees': employess})

# This method is to Edit the Employee


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

# This method is to update to Employee


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee': employee})

# This method is to Delete the Employee


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
