import random
from django.core.management.base import BaseCommand
from django.db import transaction
from application.models import Doctor, HealthIssue, Hospital

class Command(BaseCommand):
    help = 'Bulk insert doctors with assigned health issues and hospitals'

    def handle(self, *args, **kwargs):
        # List of typical Bangladeshi names for doctors
        doctor_names = [
            "Dr. Muhammad Akram", "Dr. Ayesha Sultana", "Dr. Nurul Islam", "Dr. Farhana Sultana", 
            "Dr. Shahinur Rahman", "Dr. Tareq Aziz", "Dr. Rasheda Begum", "Dr. Tanvir Rahman", 
            "Dr. Shama Akter", "Dr. Zubair Ahmed", "Dr. Momena Khatun", "Dr. Mohammad Rashed", 
            "Dr. Nasreen Sultana", "Dr. Zubair Ahmed", "Dr. Nilufa Akter", "Dr. Shamsul Huda", 
            "Dr. Nabila Chowdhury", "Dr. Morsheda Begum", "Dr. Shahnaz Begum", "Dr. Saiful Islam", 
            "Dr. Samia Ahmed", "Dr. Khaled Chowdhury", "Dr. Salma Begum", "Dr. Abdur Rahman", 
            "Dr. Nigar Sultana", "Dr. Sabiha Ali", "Dr. Akram Hossain", "Dr. Rehana Begum", 
            "Dr. Meherun Nesa", "Dr. Ibrahim Khalil", "Dr. Imran Hossain", "Dr. Rumi Akter", 
            "Dr. Ahsan Habib", "Dr. Munira Parveen", "Dr. Fakhruddin Chowdhury", "Dr. Suman Chakraborty", 
            "Dr. Rubina Binte Azad", "Dr. Aminul Islam", "Dr. Nurun Nabi", "Dr. Nasim Chowdhury", 
            "Dr. Mahbubur Rahman", "Dr. Monira Begum", "Dr. Masud Rana", "Dr. Fariha Akter", 
            "Dr. Sadaf Hossain", "Dr. Sabina Yasmin", "Dr. Rana Parveen", "Dr. Asma Begum"
        ]

        # Fetch health issues and hospitals from the database
        health_issues = HealthIssue.objects.all()
        hospitals = list(Hospital.objects.all())  # Convert QuerySet to a list

        # List to hold doctor instances
        doctors = []

        # Generate doctors
        for _ in range(2000):  # Increase the number of doctors to 2000
            doctor_name = random.choice(doctor_names)
            health_issue = random.choice(health_issues)
            assigned_hospitals = random.sample(hospitals, 2)  # Assign two hospitals to each doctor
            visiting_hours = [
                {"day": "Monday", "hours": "9:00 AM - 5:00 PM"},
                {"day": "Tuesday", "hours": "9:00 AM - 5:00 PM"},
                {"day": "Wednesday", "hours": "9:00 AM - 5:00 PM"},
                {"day": "Thursday", "hours": "9:00 AM - 5:00 PM"},
                {"day": "Friday", "hours": "9:00 AM - 5:00 PM"}
            ]

            # Create a Doctor instance without assigning hospitals yet
            doctor = Doctor(
                name=doctor_name,
                health_issue=health_issue,
                visiting_hours=visiting_hours
            )
            doctors.append(doctor)

        # Bulk insert doctors into the database
        with transaction.atomic():
            Doctor.objects.bulk_create(doctors)

        # Now assign hospitals to the doctors
        for doctor in doctors:
            # Assign the selected hospitals to the doctor
            doctor.hospitals.set(assigned_hospitals)

        self.stdout.write(self.style.SUCCESS('Successfully created 2000 doctor records with hospitals'))
