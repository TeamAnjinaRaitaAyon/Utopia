# Generated by Django 4.2.5 on 2023-10-05 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0022_mpelection_votedonelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politiciansprimarydetails',
            name='PoliticianRole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PoliticianRole', to='application.usersprimarydetails'),
        ),
    ]
