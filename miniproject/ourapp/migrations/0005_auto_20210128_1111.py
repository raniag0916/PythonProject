# Generated by Django 3.1.5 on 2021-01-28 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0004_employeedetails_employeesalary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Address',
            new_name='emp_Address',
        ),
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Email',
            new_name='emp_Email',
        ),
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Gender',
            new_name='emp_Gender',
        ),
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Name',
            new_name='emp_Name',
        ),
        migrations.RenameField(
            model_name='employeedetails',
            old_name='PNumber',
            new_name='emp_PNumber',
        ),
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Password',
            new_name='emp_Password',
        ),
    ]
