# Generated by Django 4.2.6 on 2024-12-08 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0108_delete_college_delete_school_delete_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('available_departments', models.CharField(max_length=100)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.institutiontype')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.TextField()),
                ('address', models.TextField()),
                ('available_classes', models.CharField(max_length=200)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.institutiontype')),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('available_subjects', models.CharField(max_length=100)),
                ('institution_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.institutiontype')),
            ],
        ),
    ]
