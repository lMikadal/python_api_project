from ninja import Router
from typing import List
from app_employee.models import Position
from app_employee.schema import PositionSchema, MessageSchema

router = Router()

@router.get('/', response=List[PositionSchema], tags=['position'])
def all_position(request):
    return Position.objects.all()

@router.get('/{int:p_id}', response={200: PositionSchema, 404: MessageSchema}, tags=['position'])
def one_position(request, p_id: int):
    try:
        data = Position.objects.get(pk=p_id)
    except:
        return 404, {"message": "Not found position"}
    return 200, data

@router.post('/', response={201: MessageSchema}, tags=['position'])
def add_position(request, data:PositionSchema):
    Position.objects.create(**data.dict())
    return 201, {"message": "Add position success"}

@router.put('/{int:p_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['position'])
def update_position(request, p_id: int, data:PositionSchema):
    try:
        d = Position.objects.get(pk=p_id)
    except:
        return 404, {"message": "Can't update position"}
    for attr, value in data.dict().items():
        setattr(d, attr, value)
    d.save()
    return 200, {"message": "Update success"}

@router.delete('/{int:p_id}', response={200: MessageSchema, 404: MessageSchema}, tags=['position'])
def delete_position(request, p_id: int):
    try:
        data = Position.objects.get(pk=p_id)
    except:
        return 404, {"message": "Can't delete position"}
    data.delete()
    return 200, {"message": "Delete success"}