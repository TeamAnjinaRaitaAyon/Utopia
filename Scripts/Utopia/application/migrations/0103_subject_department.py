# Generated by Django 4.2.6 on 2024-12-07 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0102_remove_class_institute_remove_department_institute_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.college')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.university')),
            ],
        ),
    ]
