# Generated by Django 3.1.5 on 2021-01-22 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0003_studentmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=20, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=20, null=True)),
                ('Gender', models.CharField(blank=True, max_length=20, null=True)),
                ('PNumber', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary', models.CharField(blank=True, max_length=20, null=True)),
                ('Empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.employeedetails')),
            ],
        ),
    ]