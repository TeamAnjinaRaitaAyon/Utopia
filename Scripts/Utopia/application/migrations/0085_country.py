# Generated by Django 4.2.11 on 2024-11-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0084_city_neighborhood_delete_userpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
