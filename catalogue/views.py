from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from catalogue.models import Employee


class EmployeeList(ListView):
    paginate_by = 25
    model = Employee

# def employee_list(request):
#     juniors = Employee.objects.filter(role='JNR')
#     paginator = Paginator(juniors, 10)
#     page_number = request.Get.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, template_name='catalogue/employee_list.html', context={'juniors': juniors, 'page_obj': page_obj})
