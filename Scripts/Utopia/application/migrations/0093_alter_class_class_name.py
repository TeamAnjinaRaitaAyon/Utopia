# Generated by Django 4.2.6 on 2024-12-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0092_application_remove_college_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.IntegerField(max_length=50),
        ),
    ]