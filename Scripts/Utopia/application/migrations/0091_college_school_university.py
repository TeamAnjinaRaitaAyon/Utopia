# Generated by Django 4.2.6 on 2024-12-05 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0090_citybook_cityride_countrybook_countryride_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('subjects', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
                ('num_classes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('num_departments', models.IntegerField()),
                ('num_rank', models.IntegerField()),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]