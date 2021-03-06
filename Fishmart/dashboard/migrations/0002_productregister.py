# Generated by Django 3.1.5 on 2021-02-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Product_Category', models.CharField(blank=True, max_length=200, null=True)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='productimage')),
                ('Product_Stock', models.CharField(blank=True, max_length=50, null=True)),
                ('Product_Quantity', models.CharField(blank=True, max_length=200, null=True)),
                ('Product_Price', models.CharField(blank=True, max_length=150, null=True)),
                ('Product_Description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
