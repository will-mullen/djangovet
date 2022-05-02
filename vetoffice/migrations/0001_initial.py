# Generated by Django 2.2 on 2022-05-02 14:45

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
            name='FB_N_01',
            fields=[
                ('ModelID', models.AutoField(primary_key=True, serialize=False)),
                ('Host', models.FloatField()),
                ('Actor', models.FloatField()),
                ('Road', models.FloatField()),
                ('Timestamp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tracking1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('VisitId', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Red_Line_Tracking',
            fields=[
                ('TrackingID', models.AutoField(primary_key=True, serialize=False)),
                ('Timestamp', models.DateField()),
                ('CombinedModelList', models.ManyToManyField(to='vetoffice.FB_N_01')),
            ],
        ),
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('modelid', models.ManyToManyField(to='vetoffice.Tracking1')),
            ],
        ),
    ]
