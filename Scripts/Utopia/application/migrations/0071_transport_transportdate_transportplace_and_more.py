# Generated by Django 4.2.6 on 2024-11-07 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0070_booking_buscategory_cartype_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransportDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TransportPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transport')),
            ],
        ),
        migrations.CreateModel(
            name='TransportSeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transport_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transportdate')),
            ],
        ),
        migrations.CreateModel(
            name='TransportTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=5)),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user_id', models.CharField(max_length=100)),
                ('seat_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transportseattype')),
                ('transport_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transportdate')),
                ('transport_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transportplace')),
                ('transport_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transport')),
            ],
        ),
        migrations.AddField(
            model_name='transportdate',
            name='transport_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.transportplace'),
        ),
    ]
