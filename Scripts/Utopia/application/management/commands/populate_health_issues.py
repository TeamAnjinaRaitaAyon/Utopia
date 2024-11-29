from django.core.management.base import BaseCommand
from application.models import HealthIssue

class Command(BaseCommand):
    help = 'Bulk insert health issues (diseases) into the database'

    def handle(self, *args, **kwargs):
        # List of health issues to insert, including female and child-oriented issues
        issues = [
            # General health issues
            "Cold", "Fever", "Asthma", "Diabetes", "Hypertension", "Cancer", "Flu", 
            "Pneumonia", "Migraine", "Arthritis", "Back pain", "Stroke", "Heart Disease", 
            "Chronic Obstructive Pulmonary Disease (COPD)", "Tuberculosis", "Malaria", 
            "Ebola", "HIV/AIDS", "COVID-19", "Kidney Disease", "Obesity", "Depression", 
            "Anxiety", "Schizophrenia", "Parkinson's Disease", "Alzheimer's Disease", 
            "Epilepsy", "Sickle Cell Disease", "Hepatitis", "Lung Cancer", "Prostate Cancer", 
            "Osteoporosis", "Psoriasis", "Lupus", "Dementia", "Celiac Disease", 
            "Irritable Bowel Syndrome", "Gout", "Hepatitis B", "Hepatitis C", "Cholesterol", 
            "Chikungunya", "Dengue", "Rabies", "Cystic Fibrosis", "Meningitis", "Zika Virus", 
            "Bipolar Disorder", "Thyroid Disease", "Multiple Sclerosis",

            # Female health issues
            "Polycystic Ovary Syndrome (PCOS)", "Endometriosis", "Fibroids", 
            "Pelvic Inflammatory Disease (PID)", "Cervical Cancer", "Menstrual Disorders",
            "Menopause", "Postpartum Depression", "Breastfeeding Issues", "Miscarriage", 
            "Pregnancy Complications", "Gestational Diabetes", "Preeclampsia", "Placenta Previa", 
            "Osteoporosis in Women", "Sexual Health Issues in Women",

            # Child health issues
            "Childhood Obesity", "Pediatric Asthma", "Childhood Cancer", "Autism Spectrum Disorder (ASD)", 
            "Attention Deficit Hyperactivity Disorder (ADHD)", "Speech and Language Delays", 
            "Premature Birth", "Low Birth Weight", "Neonatal Jaundice", "Respiratory Infections in Children", 
            "Gastrointestinal Infections", "Ear Infections in Children", "Developmental Disorders in Children", 
            "Congenital Heart Defects", "Cleft Palate", "Down Syndrome", "Accidents and Injuries in Children",
            "Mental Health Disorders in Children", "Separation Anxiety in Children", "Conduct Disorders in Children"
        ]
        
        # Iterate through the list of issues and only insert those that do not already exist
        existing_issues = HealthIssue.objects.filter(name__in=issues).values_list('name', flat=True)
        new_issues = [HealthIssue(name=issue) for issue in issues if issue not in existing_issues]
        
        # Bulk create the new health issues
        if new_issues:
            HealthIssue.objects.bulk_create(new_issues)
            self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(new_issues)} new health issues!'))
        else:
            self.stdout.write(self.style.SUCCESS('No new health issues to add. All issues already exist.'))
