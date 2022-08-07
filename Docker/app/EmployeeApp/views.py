import re
from django.shortcuts import render
# to allow other domains to access api methods
from django.views.decorators.csrf import csrf_exempt
# to parse incomming data into data model
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeesSerializer

# from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        department = Department.objects.all()
        department_serializer=DepartmentSerializer(department,many=True)
        # Safe=False: to inform django that the data we're trying to 
        # convert to Json is a valid json format
        return JsonResponse(department_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        # if the model is valid : save to DB and return success msg
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successfully to database",safe=False)
        # else return error msg
        return JsonResponse("Failed to add to database",safe=False)
    # Update a given record
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        # 1st: Capture existing record using Department Id
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        # map it to new value with serializer class
        department_serializer=DepartmentSerializer(department,data=department_data)
        # save is valid and return success msg
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated successfully to database",safe=False)
        # else return error msg
        return JsonResponse("Failed to update the data",safe=False)
    elif request.method=='DELETE':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department.delete()
        return JsonResponse("Deleted the data successfully.",safe=False)
    
    
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeesSerializer(employees,many=True)
        # Safe=False: to inform django that the data we're trying to 
        # convert to Json is a valid json format
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employees_data=JSONParser().parse(request)
        employees_serializer=EmployeesSerializer(data=employees_data)
        # if the model is valid : save to DB and return success msg
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added successfully to database",safe=False)
        # else return error msg
        return JsonResponse("Failed to add to database",safe=False)
    # Update a given record
    elif request.method=='PUT':
        employees_data=JSONParser().parse(request)
        # 1st: Capture existing record using Department Id
        employees=Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        # map it to new value with serializer class
        employees_serializer=EmployeesSerializer(employees,data=employees_data)
        # save is valid and return success msg
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated successfully to database",safe=False)
        # else return error msg
        return JsonResponse("Failed to update the data",safe=False)
    elif request.method=='DELETE':
        employees_data=JSONParser().parse(request)
        employees=Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employees.delete()
        return JsonResponse("Deleted the data successfully.",safe=False)
    
    
# @csrf_exempt
# def savefile(request):
#     file=request.FILES['file']
#     file_name=default_storage.save(file.name,file)
#     return JsonResponse(file_name,safe=False)