# Generated by Django 4.2.6 on 2024-12-08 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0112_delete_college_delete_school_delete_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('avaiable_subject', models.CharField(max_length=100)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colleges', to='application.institutiontype')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.TextField()),
                ('address', models.TextField()),
                ('type', models.CharField(max_length=10)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='application.institutiontype')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('departments_count', models.IntegerField()),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='application.institutiontype')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='application.university')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='application.school')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='application.college')),
            ],
        ),
    ]