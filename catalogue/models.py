from django.db import models


class Employee(models.Model):

    EMPLOYEE_TYPES = (
        ('JNR', 'junior'),
        ('MDL', 'middle'),
        ('SNR', 'senior'),
        ('TML', 'team lead'),
        ('MNG', 'manager'),
    )

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField(max_length=40, blank=False, null=True)
    age = models.IntegerField(blank=True)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, default='JNR')
    salary = models.IntegerField(default=0)
    employment_date = models.DateField(auto_now=True)
    manager = models.ForeignKey('self', null=True, related_name='subordinates', on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

