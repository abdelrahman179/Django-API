# Convert complex types, model instances to native python and datatypes
# that can easily rendered into json, xml or other content types and vice versa.


from rest_framework import serializers
from EmployeeApp.models import Department, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Department
        fields=('DepartmentId','DepartmentName')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')  