# Generated by Django 4.2.6 on 2024-12-07 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0103_subject_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.college')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.school')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.university')),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='college',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
