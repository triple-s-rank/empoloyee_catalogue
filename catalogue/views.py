from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from catalogue.models import Employee


def employee_list(request):

    managers = Employee.objects.filter(role='MNG')
    paginator = Paginator(managers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
      request,
      template_name='catalogue/employee_list.html',
      context={'page_obj': page_obj}
    )


class EmployeeList(ListView):
    model = Employee
    paginate_by = 50
    template_name = 'catalogue/base.html'
    context_object_name = 'workers'

    def get_queryset(self):
        return Employee.objects.all()