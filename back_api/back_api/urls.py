from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from app_employee.api.api_department import router as department_router
from app_employee.api.api_position import router as position_router
from app_employee.api.api_employee import router as employee_router

api = NinjaAPI()
api.add_router('department', department_router)
api.add_router('position', position_router)
api.add_router('employee', employee_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
