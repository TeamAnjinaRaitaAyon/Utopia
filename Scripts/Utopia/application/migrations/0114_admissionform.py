# Generated by Django 4.2.6 on 2024-12-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0113_college_school_university_universitydepartment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_type', models.CharField(max_length=100)),
                ('institution_name', models.CharField(max_length=100)),
                ('class_subject_department', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]