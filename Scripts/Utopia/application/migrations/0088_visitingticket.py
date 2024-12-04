# Generated by Django 4.2.11 on 2024-12-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0087_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitingTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('username', models.CharField(max_length=255)),
                ('health_issue_name', models.CharField(max_length=255)),
                ('hospital_type', models.CharField(max_length=50)),
                ('hospital_name', models.CharField(max_length=255)),
                ('doctor_name', models.CharField(max_length=255)),
                ('visiting_hour', models.CharField(max_length=50)),
            ],
        ),
    ]
