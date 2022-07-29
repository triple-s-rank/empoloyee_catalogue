from django.urls import path

from catalogue import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name='employee_list_url')
]