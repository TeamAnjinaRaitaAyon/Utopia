# Generated by Django 4.2.6 on 2024-12-07 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0101_rename_schoolclass_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='department',
            name='institute',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='institute',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Institute',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
