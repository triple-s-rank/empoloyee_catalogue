from django.urls import path

from catalogue import views

urlpatterns = [
    path('', views.employee_list, name='employee_list_url')
]
