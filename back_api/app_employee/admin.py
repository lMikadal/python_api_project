from django.contrib import admin
from app_employee.models import Department, Position, Employee

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "department"]
    
class PositionAdmin(admin.ModelAdmin):
    list_display = ["id", "position"]
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "f_name",
        "l_name",
        "age",
        "gender",
        "phone",
        "department_code",
        "position_id",
        "salary",
        "date_start",
	]
    
    @admin.display(ordering="department__code")
    def department_code(self, obj):
        return obj.department.code
    
    @admin.display(ordering="position__id")
    def position_id(self, obj):
        return obj.position.id

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)