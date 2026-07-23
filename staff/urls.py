from django.urls import path
from . import views

app_name = "staff"

urlpatterns = [
    path("list/", views.employee_list, name="list"),
    path('new/', views.employee_new, name='new'),
    path('edit/<int:employee_id>/', views.employee_edit, name='edit'),
    path('delete/<int:employee_id>/', views.employee_delete, name='delete'),
    path("<int:employee_id>/", views.employee_detail, name="detail"),
]
