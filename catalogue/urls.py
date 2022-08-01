from django.urls import path

from catalogue import views

urlpatterns = [
    path('teams', views.employee_list, name='employee_list_url'),
    path('all/', views.EmployeeList.as_view(), name='all'),
    path('all/ordered_by_name/', views.OrderByName.as_view(), name='ordered_by_name'),
    path('all/ordered_by_name_reverse/', views.OrderByNameReverse.as_view(), name='ordered_by_name_reverse'),
    path('all/ordered_by_age/', views.OrderByAge.as_view(), name='ordered_by_age'),
    path('all/ordered_by_age_reverse/', views.OrderByAgeReverse.as_view(), name='ordered_by_age_reverse'),
    path('all/ordered_by_position/', views.OrderByPosition.as_view(), name='ordered_by_position'),
    path('all/ordered_by_position_reverse/', views.OrderByPositionReverse.as_view(), name='ordered_by_position_reverse'),
    path('all/ordered_by_salary/', views.OrderBySalary.as_view(), name='ordered_by_salary'),
    path('all/ordered_by_salary_reverse/', views.OrderBySalaryReverse.as_view(), name='ordered_by_salary_reverse'),
    path('employee/<slug:slug>/', views.EmployeeDetail.as_view(), name='employee_detail')
]
