# Generated by Django 4.0.6 on 2022-07-29 16:05
import random

from django.db import migrations


def connect_roles(apps, schema_editor):
    Employee = apps.get_model('catalogue', 'Employee')

    juniors = Employee.objects.filter(role='JNR')
    middles = Employee.objects.filter(role='MDL')
    seniors = Employee.objects.filter(role='SNR')
    team_leads = Employee.objects.filter(role='TML')
    managers = Employee.objects.filter(role='MNG')

    all_roles = juniors, middles, seniors, team_leads, managers

    for count, role in enumerate(all_roles):
        for worker in role:
            if not worker.manager:
                try:
                    worker.manager = random.choice(all_roles[count + 1])
                    worker.save()
                except IndexError:
                    pass


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20220727_1539'),
    ]

    operations = [
        migrations.RunPython(connect_roles)
    ]