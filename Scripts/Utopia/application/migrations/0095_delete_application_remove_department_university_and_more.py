# Generated by Django 4.2.6 on 2024-12-06 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0094_rename_class_name_class_class_n'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.RemoveField(
            model_name='department',
            name='university',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='college',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
