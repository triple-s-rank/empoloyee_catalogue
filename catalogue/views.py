from django.shortcuts import render

from catalogue.models import Employee


def index(request):
    juniors = Employee.objects.filter(role='JNR')
    return render(request, template_name='employee_list.html', context={'juniors': juniors})
