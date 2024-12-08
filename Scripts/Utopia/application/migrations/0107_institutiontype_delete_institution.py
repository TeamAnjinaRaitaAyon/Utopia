# Generated by Django 4.2.6 on 2024-12-07 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0106_remove_schoolclass_school_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
    ]
