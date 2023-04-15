from ninja import ModelSchema, Schema
from app_employee.models import Employee, Department, Position

class DepartmentSchema(ModelSchema):
    class Config:
        model = Department
        model_fields = ['code', 'department']
        
class PositionSchema(ModelSchema):
    class Config:
        model = Position
        model_fields = ['position']
        
class EmployeeSchema(ModelSchema):
    class Config:
        model = Employee
        model_fields = ["f_name", "l_name", "age", "gender", "phone", "department", "position", "salary", "date_start"]
        
class MessageSchema(Schema):
    message: str