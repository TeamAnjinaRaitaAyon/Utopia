# Generated by Django 4.2.5 on 2023-10-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_politiciansprimarydetails_politicianname'),
    ]

    operations = [
        migrations.CreateModel(
            name='MPElection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate1ID', models.IntegerField()),
                ('Candidate2ID', models.IntegerField()),
                ('Candidate1Vote', models.IntegerField()),
                ('Candidate2Vote', models.IntegerField()),
                ('ElectionStatus', models.BooleanField()),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
            ],
        ),
    ]