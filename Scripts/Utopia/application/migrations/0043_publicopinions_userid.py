# Generated by Django 4.2.5 on 2023-10-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0042_alter_publicopinions_opinionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicopinions',
            name='UserID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
