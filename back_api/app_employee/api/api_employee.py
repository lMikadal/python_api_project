from ninja import Router
from typing import List
from app_employee.models import Employee
from app_employee.schema import EmployeeSchema, MessageSchema

router = Router()

@router.get('/', response=List[EmployeeSchema], tags=['employee'])
def all_employee(request):
    return Employee.objects.all()

@router.get('/{int:e_id}', response={200: EmployeeSchema, 404: MessageSchema}, tags=['employee'])
def one_employee(request, e_id: int):
    try:
        data = Employee.objects.get(pk=e_id)
    except:
        return 404, {"message": "Not found employee"}
    return 200, data

@router.post('/', response={201: MessageSchema}, tags=['employee'])
def add_employee(request, data:EmployeeSchema):
    Employee.objects.create(**data.dict())
    return 201, {"message": "Add employee success"}

@router.put('/{int:e_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['employee'])
def update_employee(request, e_id: int, data:EmployeeSchema):
    try:
        d = Employee.objects.get(pk=e_id)
    except:
        return 404, {"message": "Can't update employee"}
    for attr, value in data.dict().items():
        setattr(d, attr, value)
    d.save()
    return 200, {"message": "Update success"}

@router.delete('/{int:e_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['employee'])
def delete_employee(request, e_id: int):
    try:
        data = Employee.objects.get(pk=e_id)
    except:
        return 404, {"message": "Can't delete employee"}
    data.delete()
    return 200, {"message": "Delete success"}