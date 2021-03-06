# Generated by Django 3.1.5 on 2021-03-04 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0006_reciperegister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cart_Quantity', models.IntegerField(blank=True, null=True)),
                ('Cart_Price', models.IntegerField(blank=True, null=True)),
                ('Productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.productregister')),
            ],
        ),
    ]
