from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add_emp(request):
    
    deps = Department.objects.all()
    Roles = Role.objects.all()
    context = {'deps':deps, 'Role':Roles}
    
    if request.method == "POST": 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = request.POST['dept']
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])


        new_emp = Employee(
        first_name = first_name,
        last_name = last_name,
        salary = salary,
        bonus = bonus,
        dept_id = dept,
        role_id = role,
        phone = phone)

        new_emp.save()
        return HttpResponse("New employee added successfully")

   
    return render(request, 'add_emp.html', context)

def view_emp(request):

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'view_emp.html', context)


def remove_emp(request, emp_id = 0):

    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee remove sucessfully ")
        except:
            return HttpResponse("Employee does not exists, please select a valid employee")

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    
    emps = Employee.objects.all()
    if request.method == 'POST':

        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name = dept ))
        if role:
            emps = emps.filter(Q(role__name = role))

        context = {'emps':emps}
        return render(request, 'view_emp.html', context)

    return render(request, 'filter_emp.html')