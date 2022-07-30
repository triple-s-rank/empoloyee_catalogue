from django.urls import path

from catalogue import views

urlpatterns = [
    path('teams', views.employee_list, name='employee_list_url'),
    path('all/', views.EmployeeList.as_view(), name='all'),
]
