from ninja import Router
from typing import List
from app_employee.models import Department
from app_employee.schema import DepartmentSchema, MessageSchema

router = Router()

@router.get('/', response=List[DepartmentSchema], tags=['department'])
def all_department(request):
    return Department.objects.all()

@router.get('/{int:d_id}', response={200: DepartmentSchema, 404: MessageSchema}, tags=['department'])
def one_department(request, d_id: int):
    try:
        data = Department.objects.get(pk=d_id)
    except:
        return 404, {"message": "Not found Department"}
    return 200, data

@router.post('/', response={201: MessageSchema}, tags=['department'])
def add_department(request, data:DepartmentSchema):
    Department.objects.create(**data.dict())
    return 201, {"message": "Add department success"}

@router.put('/{int:d_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['department'])
def update_department(request, d_id: int, data:DepartmentSchema):
    try:
        d = Department.objects.get(pk=d_id)
    except:
        return 404, {"message": "Can't update Department"}
    for attr, value in data.dict().items():
        setattr(d, attr, value)
    d.save()
    return 200, {"message": "Update success"}

@router.delete('/{int:d_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['department'])
def delete_department(request, d_id: int):
    try:
        data = Department.objects.get(pk=d_id)
    except:
        return 404, {"message": "Can't delete department"}
    data.delete()
    return 200, {"message": "Delete success"}