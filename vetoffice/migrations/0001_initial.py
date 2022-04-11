# Generated by Django 2.2 on 2022-04-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('CustomerID', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=500)),
                ('CustomerAddress', models.CharField(max_length=500)),
                ('CustomerPhone', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('VisitId', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=500)),
            ],
        ),
    ]
