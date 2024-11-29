from application.models import Hospital, HealthIssue

# Complete list of health issues
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

    # Female-specific health issues
    "Polycystic Ovary Syndrome (PCOS)", "Endometriosis", "Fibroids", 
    "Pelvic Inflammatory Disease (PID)", "Cervical Cancer", "Menstrual Disorders",
    "Menopause", "Postpartum Depression", "Breastfeeding Issues", "Miscarriage", 
    "Pregnancy Complications", "Gestational Diabetes", "Preeclampsia", "Placenta Previa", 
    "Osteoporosis in Women", "Sexual Health Issues in Women",

    # Child-specific health issues
    "Childhood Obesity", "Pediatric Asthma", "Childhood Cancer", "Autism Spectrum Disorder (ASD)", 
    "Attention Deficit Hyperactivity Disorder (ADHD)", "Speech and Language Delays", 
    "Premature Birth", "Low Birth Weight", "Neonatal Jaundice", "Respiratory Infections in Children", 
    "Gastrointestinal Infections", "Ear Infections in Children", "Developmental Disorders in Children", 
    "Congenital Heart Defects", "Cleft Palate", "Down Syndrome", "Accidents and Injuries in Children",
    "Mental Health Disorders in Children", "Separation Anxiety in Children", "Conduct Disorders in Children"
]


# List of hospitals and their treated issues (updated for broader coverage)
hospital_data = [
    {
        "name": "Bangabandhu Sheikh Mujib Medical University (BSMMU)",
        "type": "Public",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Diabetes", "Hypertension", "COVID-19", 
            "Thyroid Disease", "Multiple Sclerosis", "Bipolar Disorder", "Parkinson's Disease", 
            "Schizophrenia", "Anxiety", "Depression", "Osteoporosis", "Lupus", "Psoriasis", 
            "Celiac Disease", "Dementia", "Prostate Cancer", "Preeclampsia", 
            "Childhood Cancer", "Congenital Heart Defects", "Respiratory Infections in Children"
        ]
    },
    {
        "name": "Dhaka Medical College and Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", "Dengue", "Chikungunya", 
            "Hepatitis B", "Hepatitis C", "Malaria", "Chronic Obstructive Pulmonary Disease (COPD)", 
            "Kidney Disease", "Back pain", "Migraine", "Mental Health Disorders in Children", 
            "Gastrointestinal Infections"
        ]
    },
    {
        "name": "Square Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Lung Cancer", "Diabetes", "Hypertension", "Obesity", "Depression", 
            "Polycystic Ovary Syndrome (PCOS)", "Endometriosis", "Pregnancy Complications", 
            "Autism Spectrum Disorder (ASD)", "Pediatric Asthma", "Breastfeeding Issues"
        ]
    },
    {
        "name": "United Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "COVID-19", "Epilepsy", "Prostate Cancer", 
            "Alzheimer's Disease", "Anxiety", "Stroke", "Heart Disease", 
            "Osteoporosis in Women", "Sexual Health Issues in Women", 
            "Developmental Disorders in Children", "Speech and Language Delays"
        ]
    },
    {
        "name": "BIRDEM General Hospital",
        "type": "Public",
        "issues": [
            "Diabetes", "Kidney Disease", "Thyroid Disease", "Obesity", "Depression", 
            "Polycystic Ovary Syndrome (PCOS)", "Gestational Diabetes", "Premature Birth", 
            "Menopause", "Menstrual Disorders", "Down Syndrome"
        ]
    },
    {
        "name": "Apollo Hospital (Evercare)",
        "type": "Private",
        "issues": [
            "Cancer", "Thyroid Disease", "Lupus", "Psoriasis", "Asthma", 
            "Ebola", "HIV/AIDS", "Endometriosis", "Cervical Cancer", 
            "Pelvic Inflammatory Disease (PID)", "Breastfeeding Issues", 
            "Accidents and Injuries in Children"
        ]
    },
    {
        "name": "Chittagong Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", "Dengue", "Pneumonia", 
            "Rabies", "Meningitis", "Autism Spectrum Disorder (ASD)", 
            "Mental Health Disorders in Children", "Conduct Disorders in Children"
        ]
    },
    {
        "name": "Holy Family Red Crescent Medical College Hospital",
        "type": "Private",
        "issues": [
            "Bipolar Disorder", "Alzheimer's Disease", "Parkinson's Disease", 
            "Diabetes", "Schizophrenia", "Anxiety", "Pregnancy Complications", 
            "Miscarriage", "Low Birth Weight", "Cleft Palate"
        ]
    },
    {
        "name": "National Institute of Cardiovascular Diseases (NICVD)",
        "type": "Public",
        "issues": [
            "Heart Disease", "Stroke", "Hypertension", "Cholesterol", 
            "Chronic Obstructive Pulmonary Disease (COPD)", "Kidney Disease"
        ]
    },
    {
        "name": "Kurmitola General Hospital",
        "type": "Public",
        "issues": [
            "COVID-19", "Dengue", "Chikungunya", "Flu", "Asthma", 
            "Pneumonia", "Neonatal Jaundice", "Respiratory Infections in Children"
        ]
    }
]
hospital_data.extend([
    {
        "name": "Ibrahim Cardiac Hospital & Research Institute",
        "type": "Private",
        "issues": [
            "Heart Disease", "Hypertension", "Stroke", "Cholesterol", "Diabetes",
            "Congenital Heart Defects", "Arrhythmia", "Heart Valve Disease", 
            "Pulmonary Hypertension"
        ]
    },
    {
        "name": "National Institute of Mental Health (NIMH)",
        "type": "Public",
        "issues": [
            "Schizophrenia", "Bipolar Disorder", "Depression", "Anxiety", 
            "Obsessive-Compulsive Disorder (OCD)", "Substance Abuse", 
            "Eating Disorders", "Post-Traumatic Stress Disorder (PTSD)"
        ]
    },
    {
        "name": "Holy Family Red Crescent Medical College Hospital",
        "type": "Private",
        "issues": [
            "Gynecological Issues", "Endometriosis", "Menstrual Disorders", 
            "Pregnancy Complications", "Postpartum Depression", 
            "Sexual Health Issues in Women", "Breastfeeding Issues"
        ]
    },
    {
        "name": "Labaid Specialized Hospital",
        "type": "Private",
        "issues": [
            "Cardiology", "Cancer", "Gastroenterology", "Neurology", 
            "Orthopedics", "Nephrology", "Diabetes", "Hypertension", 
            "Pediatrics", "Dermatology"
        ]
    },
    {
        "name": "National Institute of Traumatology & Orthopedic Rehabilitation (NITOR)",
        "type": "Public",
        "issues": [
            "Fractures", "Arthritis", "Back pain", "Spinal Cord Injury", 
            "Sports Injuries", "Joint Replacement", "Bone Tumors", 
            "Muscle Disorders", "Osteoporosis"
        ]
    },
    {
        "name": "Enam Medical College & Hospital",
        "type": "Private",
        "issues": [
            "General Surgery", "Gynecology", "Pediatrics", "Orthopedics", 
            "Neurology", "Cardiology", "ENT (Ear, Nose, and Throat)", 
            "Dental Care", "Emergency Medicine"
        ]
    },
    {
        "name": "Ibn Sina Specialized Hospital",
        "type": "Private",
        "issues": [
            "Nephrology", "Endocrinology", "Cardiology", "Dermatology", 
            "Oncology", "Orthopedics", "Neurology", "Pulmonology", 
            "Rheumatology"
        ]
    },
    {
        "name": "Mugda Medical College and Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", "Hypertension", 
            "Diabetes", "Pneumonia", "Hepatitis", "Flu", "Rabies"
        ]
    },
    {
        "name": "Kuwait Bangladesh Friendship Government Hospital",
        "type": "Public",
        "issues": [
            "COVID-19", "Chikungunya", "Dengue", "Respiratory Infections in Children", 
            "Neonatal Jaundice", "Childhood Obesity", "Diabetes", "General Surgery"
        ]
    },
    {
        "name": "Ad-din Women's Medical College Hospital",
        "type": "Private",
        "issues": [
            "Gynecological Issues", "Pregnancy Complications", "Menopause", 
            "Osteoporosis in Women", "Breast Cancer", "Cervical Cancer", 
            "Infertility Issues", "Endometriosis"
        ]
    },
    {
        "name": "Popular Diagnostic Centre Ltd.",
        "type": "Private",
        "issues": [
            "General Checkups", "Cancer Screening", "Diabetes", 
            "Heart Disease", "Thyroid Disorders", "Kidney Disease", 
            "Cholesterol", "General Surgery", "Imaging & Diagnostics"
        ]
    },
    {
        "name": "Sir Salimullah Medical College & Mitford Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Hypertension", "Stroke", 
            "Tuberculosis", "Malaria", "Rabies", "Meningitis", "Dengue"
        ]
    },
    {
        "name": "Combined Military Hospital (CMH) Dhaka",
        "type": "Public",
        "issues": [
            "Trauma Care", "Orthopedics", "Cardiology", "Neurology", 
            "Diabetes", "Hypertension", "Cancer", "Infectious Diseases", 
            "Mental Health Issues", "Child Health"
        ]
    },
    {
        "name": "Delta Medical College and Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Asthma", "Diabetes", "Hypertension", 
            "Tuberculosis", "General Surgery", "Orthopedics", 
            "ENT", "Pediatrics", "Gynecology"
        ]
    },
    {
        "name": "Dhaka Shishu (Children) Hospital",
        "type": "Public",
        "issues": [
            "Pediatric Asthma", "Childhood Obesity", "Premature Birth", 
            "Developmental Disorders", "Gastrointestinal Infections", 
            "Congenital Heart Defects", "Neonatal Jaundice", 
            "Speech and Language Delays", "Autism Spectrum Disorder (ASD)"
        ]
    }
])

hospital_data.extend([
    {
        "name": "Rajshahi Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Malaria", "Tuberculosis", "Diabetes", 
            "Asthma", "Hypertension", "Pneumonia", "Gastrointestinal Infections", 
            "Respiratory Diseases"
        ]
    },
    {
        "name": "Sylhet MAG Osmani Medical College Hospital",
        "type": "Public",
        "issues": [
            "Dengue", "Chikungunya", "Cold", "Fever", "Meningitis", 
            "Kidney Disease", "Diabetes", "Stroke", "Hypertension", 
            "Gastrointestinal Disorders"
        ]
    },
    {
        "name": "Mymensingh Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Heart Disease", "Diabetes", 
            "Hypertension", "Thyroid Disorders", "Tuberculosis", 
            "Pediatric Infectious Diseases", "Snake Bite"
        ]
    },
    {
        "name": "Anwer Khan Modern Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cardiology", "Neurology", "Orthopedics", "General Surgery", 
            "Gynecology", "Diabetes", "Hypertension", "Gastroenterology", 
            "Dermatology", "ENT"
        ]
    },
    {
        "name": "Northern International Medical College & Hospital",
        "type": "Private",
        "issues": [
            "General Medicine", "Gynecology", "Pediatrics", "Orthopedics", 
            "Diabetes", "Hypertension", "Chronic Obstructive Pulmonary Disease (COPD)", 
            "Dental Care", "Childhood Infections", "Heart Disease"
        ]
    },
    {
        "name": "Uttara Adhunik Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", "Diabetes", 
            "Gynecological Issues", "Heart Disease", "Hypertension", 
            "Kidney Disease", "Orthopedic Conditions"
        ]
    },
    {
        "name": "Shaheed Suhrawardy Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Heart Disease", "Asthma", "Diabetes", "Hypertension", 
            "Respiratory Infections", "Cancer", "Stroke", "Dengue", 
            "Malnutrition in Children", "Gastrointestinal Issues"
        ]
    },
    {
        "name": "Marks Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Cardiology", "Neurology", 
            "Orthopedics", "Gynecology", "Asthma", "Cancer Screening", 
            "Mental Health Disorders", "Liver Diseases"
        ]
    },
    {
        "name": "Z H Sikder Women's Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Gynecological Issues", "Pregnancy Complications", "Breast Cancer", 
            "Cervical Cancer", "Diabetes", "Menstrual Disorders", 
            "Fertility Issues", "Menopause", "Thyroid Disease", 
            "Sexual Health"
        ]
    },
    {
        "name": "Chattogram Maa-O-Shishu Hospital Medical College",
        "type": "Private",
        "issues": [
            "Pediatric Care", "Childhood Obesity", "Premature Birth", 
            "Diabetes", "Asthma in Children", "Infectious Diseases in Children", 
            "Thalassemia", "Congenital Anomalies", "Heart Diseases in Children", 
            "Vaccination Services"
        ]
    },
    {
        "name": "National Institute of Ophthalmology & Hospital",
        "type": "Public",
        "issues": [
            "Cataract", "Glaucoma", "Refractive Errors", "Diabetic Retinopathy", 
            "Macular Degeneration", "Retinal Diseases", "Conjunctivitis", 
            "Eye Injuries", "Corneal Diseases", "Pediatric Eye Disorders"
        ]
    },
    {
        "name": "Ibn Sina Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cardiology", "Endocrinology", "General Surgery", "ENT", 
            "Neurology", "Orthopedics", "Pediatrics", "Gastroenterology", 
            "Gynecology", "Ophthalmology"
        ]
    },
    {
        "name": "Pabna Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", "Diabetes", 
            "Hypertension", "Heart Disease", "Infectious Diseases", 
            "Orthopedic Conditions", "Childhood Malnutrition"
        ]
    },
    {
        "name": "Rangpur Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Diabetes", "Heart Disease", 
            "Stroke", "Tuberculosis", "Pneumonia", "Rabies", 
            "Kidney Disease"
        ]
    },
    {
        "name": "Barishal Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Dengue", "Diabetes", "Asthma", 
            "Hypertension", "Thyroid Disorders", "Infectious Diseases", 
            "Malnutrition in Children", "General Surgery"
        ]
    },
    {
        "name": "Bangladesh Institute of Research and Rehabilitation in Diabetes, Endocrine and Metabolic Disorders (BIRDEM) 2",
        "type": "Public",
        "issues": [
            "Diabetes", "Obesity", "Thyroid Disorders", "Hormonal Imbalance", 
            "Metabolic Disorders", "Kidney Disease", "Eye Complications from Diabetes", 
            "Neuropathy", "Cardiovascular Complications from Diabetes"
        ]
    }
])
hospital_data += [
    {
        "name": "Ibrahim Cardiac Hospital & Research Institute",
        "type": "Private",
        "issues": [
            "Heart Disease", "Stroke", "Hypertension", "Cholesterol", 
            "Chronic Obstructive Pulmonary Disease (COPD)", "Kidney Disease", 
            "Prostate Cancer", "Thyroid Disease", "Osteoporosis", "Gout"
        ]
    },
    {
        "name": "National Institute of Mental Health & Hospital",
        "type": "Public",
        "issues": [
            "Schizophrenia", "Bipolar Disorder", "Depression", "Anxiety", 
            "Alzheimer's Disease", "Parkinson's Disease", "Epilepsy", "Dementia", 
            "Autism Spectrum Disorder (ASD)", "Conduct Disorders in Children"
        ]
    },
    {
        "name": "Labaid Specialized Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Lung Cancer", "Liver Disease", "Heart Disease", 
            "Diabetes", "Hypertension", "Obesity", "Gastrointestinal Infections", 
            "Migraine", "Kidney Disease"
        ]
    },
    {
        "name": "Dhaka Shishu (Children) Hospital",
        "type": "Public",
        "issues": [
            "Pediatric Asthma", "Autism Spectrum Disorder (ASD)", 
            "Premature Birth", "Low Birth Weight", "Neonatal Jaundice", 
            "Developmental Disorders in Children", "Respiratory Infections in Children", 
            "Congenital Heart Defects", "Down Syndrome", "Speech and Language Delays"
        ]
    },
    {
        "name": "Combined Military Hospital (CMH) Dhaka",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Back pain", "Diabetes", 
            "Thyroid Disease", "Hypertension", "COVID-19", "Migraine", 
            "Respiratory Infections in Children", "Neonatal Jaundice"
        ]
    },
    {
        "name": "Ad-Din Women's Medical College Hospital",
        "type": "Private",
        "issues": [
            "Polycystic Ovary Syndrome (PCOS)", "Endometriosis", 
            "Pregnancy Complications", "Breastfeeding Issues", 
            "Gestational Diabetes", "Menopause", "Postpartum Depression", 
            "Sexual Health Issues in Women", "Miscarriage", "Cervical Cancer"
        ]
    },
    {
        "name": "National Institute of Traumatology and Orthopaedic Rehabilitation (NITOR)",
        "type": "Public",
        "issues": [
            "Back pain", "Arthritis", "Bone Fractures", "Spinal Cord Injuries", 
            "Osteoporosis", "Sports Injuries", "Joint Replacement", "Scoliosis", 
            "Osteoarthritis", "Rheumatoid Arthritis"
        ]
    },
    {
        "name": "Central Hospital Limited",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Diabetes", "Thyroid Disease", 
            "Asthma", "Tuberculosis", "Migraine", "Heart Disease", 
            "Gastrointestinal Infections", "Chronic Obstructive Pulmonary Disease (COPD)"
        ]
    },
    {
        "name": "Enam Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Asthma", "Back pain", "Kidney Disease", 
            "COVID-19", "Flu", "Stroke", "Heart Disease", 
            "Migraine", "Chronic Obstructive Pulmonary Disease (COPD)"
        ]
    },
    {
        "name": "Sir Salimullah Medical College and Mitford Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Tuberculosis", "Hepatitis B", "Hepatitis C", 
            "Diabetes", "COVID-19", "Thyroid Disease", "Dengue", 
            "Chikungunya", "Hypertension"
        ]
    },
    {
        "name": "Popular Diagnostic Centre",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Heart Disease", "Kidney Disease", 
            "Thyroid Disease", "Obesity", "Gout", "Osteoporosis", 
            "Migraine", "Respiratory Infections in Children"
        ]
    },
    {
        "name": "Japan East-West Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Asthma", "Tuberculosis", "Diabetes", 
            "Heart Disease", "Stroke", "Kidney Disease", 
            "Pediatric Asthma", "Congenital Heart Defects", "Autism Spectrum Disorder (ASD)"
        ]
    },
    {
        "name": "Shaheed Suhrawardy Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Tuberculosis", 
            "Diabetes", "Kidney Disease", "Chronic Obstructive Pulmonary Disease (COPD)", 
            "COVID-19", "Gastrointestinal Infections", "Chikungunya"
        ]
    }
]
hospital_data += [
    {
        "name": "Bangladesh Eye Hospital & Institute",
        "type": "Private",
        "issues": [
            "Cataract", "Glaucoma", "Diabetic Retinopathy", 
            "Macular Degeneration", "Refractive Errors", "Eye Infections", 
            "Retinal Detachment", "Dry Eye Syndrome", "Corneal Diseases", 
            "Pediatric Eye Disorders"
        ]
    },
    {
        "name": "National Institute of Cancer Research & Hospital (NICRH)",
        "type": "Public",
        "issues": [
            "Lung Cancer", "Breast Cancer", "Colon Cancer", 
            "Prostate Cancer", "Cervical Cancer", "Leukemia", 
            "Lymphoma", "Ovarian Cancer", "Pancreatic Cancer", 
            "Liver Cancer", "Childhood Cancer"
        ]
    },
    {
        "name": "International Centre for Diarrhoeal Disease Research, Bangladesh (ICDDR,B)",
        "type": "Public",
        "issues": [
            "Diarrhea", "Cholera", "Gastrointestinal Infections", 
            "Malnutrition", "Dengue", "Typhoid Fever", 
            "Influenza", "Tuberculosis", "HIV/AIDS", 
            "Viral Hepatitis", "Respiratory Infections"
        ]
    },
    {
        "name": "Kumudini Women's Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Pregnancy Complications", "Breast Cancer", "Cervical Cancer", 
            "Gestational Diabetes", "Menstrual Disorders", "Polycystic Ovary Syndrome (PCOS)", 
            "Menopause", "Postpartum Depression", "Sexual Health Issues", 
            "Low Birth Weight", "Infertility"
        ]
    },
    {
        "name": "Delta Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Tuberculosis", "Diabetes", 
            "Hypertension", "Asthma", "Kidney Disease", 
            "COVID-19", "Thyroid Disease", "Heart Disease"
        ]
    },
    {
        "name": "National Institute of Kidney Diseases & Urology (NIKDU)",
        "type": "Public",
        "issues": [
            "Kidney Disease", "Urinary Tract Infections", "Prostate Disorders", 
            "Bladder Cancer", "Kidney Stones", "Chronic Kidney Disease", 
            "Glomerulonephritis", "Nephrotic Syndrome", "Dialysis Management", 
            "Urinary Incontinence"
        ]
    },
    {
        "name": "Pangu Hospital (National Institute of Traumatology & Orthopaedic Rehabilitation)",
        "type": "Public",
        "issues": [
            "Bone Fractures", "Osteoarthritis", "Scoliosis", 
            "Joint Replacement", "Rheumatoid Arthritis", "Sports Injuries", 
            "Back pain", "Spinal Cord Injuries", "Carpal Tunnel Syndrome", 
            "Clubfoot"
        ]
    },
    {
        "name": "Ibn Sina Hospital",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Heart Disease", "Asthma", 
            "Thyroid Disease", "Obesity", "Migraine", 
            "Kidney Disease", "Tuberculosis", "Thalassemia"
        ]
    },
    {
        "name": "Medinova Medical Services",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Diabetes", "Thyroid Disease", 
            "Heart Disease", "COVID-19", "Asthma", 
            "Hypertension", "Gastrointestinal Infections", "Chronic Obstructive Pulmonary Disease (COPD)"
        ]
    },
    {
        "name": "Anwar Khan Modern Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Tuberculosis", "Kidney Disease", 
            "Heart Disease", "Stroke", "COVID-19", 
            "Migraine", "Back pain", "Diabetes"
        ]
    },
    {
        "name": "Sheikh Hasina National Institute of Burn and Plastic Surgery",
        "type": "Public",
        "issues": [
            "Burn Injuries", "Skin Grafts", "Plastic Surgery", 
            "Reconstructive Surgery", "Facial Injuries", "Cleft Lip and Palate", 
            "Scar Revision", "Skin Cancer", "Accident-Related Injuries"
        ]
    },
    {
        "name": "Zainul Haque Sikder Women's Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Gynecological Issues", "Pregnancy Complications", "Breast Cancer", 
            "Ovarian Cancer", "Polycystic Ovary Syndrome (PCOS)", "Endometriosis", 
            "Menstrual Disorders", "Sexual Health Issues", "Pregnancy Loss", 
            "Postpartum Depression"
        ]
    },
    {
        "name": "Bangladesh Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Diabetes", "Thyroid Disease", 
            "Heart Disease", "Kidney Disease", "Hypertension", 
            "Tuberculosis", "Back pain", "Migraine"
        ]
    },
    {
        "name": "Gonoshasthaya Nagar Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Asthma", "Tuberculosis", "Diabetes", 
            "Heart Disease", "Hypertension", "COVID-19", 
            "Gastrointestinal Infections", "Thyroid Disease", "Stroke"
        ]
    }
]

hospital_data.extend([
    {
        "name": "Medinova Medical Services",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Cancer", "Stroke", "Obesity", "Chronic Obstructive Pulmonary Disease (COPD)",
            "Mental Health Disorders", "Kidney Disease", "Asthma", "Cold", "Fever", "Flu"
        ]
    },
    {
        "name": "National Institute of Cancer Research & Hospital",
        "type": "Public",
        "issues": [
            "Cancer", "Lung Cancer", "Prostate Cancer", "Breast Cancer", "Blood Cancer", "Leukemia",
            "Liver Cancer", "Esophageal Cancer", "Ovarian Cancer", "Pancreatic Cancer"
        ]
    },
    {
        "name": "City Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Stroke", "Hypertension", "Diabetes", "Asthma", "Kidney Disease",
            "Obesity", "Back Pain", "Chronic Fatigue Syndrome", "Gout", "Psoriasis"
        ]
    },
    {
        "name": "Shahabuddin Medical College Hospital",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Cancer", "Asthma", "Obesity", "Pneumonia", "Heart Disease"
        ]
    },
    {
        "name": "Chattogram Maa-O-Shishu Hospital",
        "type": "Public",
        "issues": [
            "Childhood Obesity", "Pediatric Asthma", "Premature Birth", "Low Birth Weight", "Neonatal Jaundice",
            "Respiratory Infections in Children", "Cleft Palate", "Down Syndrome"
        ]
    },
    {
        "name": "LabAid Specialized Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Lung Cancer", "Liver Disease", "Heart Disease", "Stroke", "Diabetes", "Arthritis",
            "Obesity", "High Cholesterol", "Gastrointestinal Disorders"
        ]
    },
    {
        "name": "Bangladesh Medical College Hospital",
        "type": "Private",
        "issues": [
            "Thyroid Disease", "Bipolar Disorder", "Mental Health Disorders", "Obesity", "Hypertension", "Asthma"
        ]
    },
    {
        "name": "Rangpur Medical College Hospital",
        "type": "Public",
        "issues": [
            "Tuberculosis", "Dengue", "Asthma", "Cold", "Flu", "Pneumonia", "Cancer", "Chronic Diseases"
        ]
    },
    {
        "name": "Pabna Medical College Hospital",
        "type": "Public",
        "issues": [
            "Hypertension", "Diabetes", "Stroke", "Mental Health Disorders", "Pneumonia", "Respiratory Infections"
        ]
    },
    {
        "name": "Mugda Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Diabetes", "Hypertension", "Cancer", "Back pain", "Gout"
        ]
    },
    {
        "name": "Shaheed Suhrawardy Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Cancer", "Hypertension", "Heart Disease", "Diabetes", "Stroke", "Asthma", "Obesity", "Chronic Diseases"
        ]
    },
    {
        "name": "Islami Bank Hospital",
        "type": "Private",
        "issues": [
            "Diabetes", "Asthma", "Hypertension", "Cancer", "Stroke", "Obesity", "Back Pain"
        ]
    },
    {
        "name": "Kumudini Women's Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Pregnancy Complications", "Cervical Cancer", "Breast Cancer", "Polycystic Ovary Syndrome (PCOS)",
            "Menstrual Disorders", "Menopause", "Fertility Issues"
        ]
    },
    {
        "name": "Savar Hospital",
        "type": "Private",
        "issues": [
            "Cold", "Fever", "Asthma", "Pneumonia", "Diabetes", "Hypertension", "Back pain"
        ]
    },
    {
        "name": "MedeAnalytics Healthcare",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Diabetes", "Asthma", "Obesity", "Chronic Pain", "Back pain"
        ]
    },
    {
        "name": "North South Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Diabetes", "Hypertension", "Kidney Disease", "Chronic Respiratory Diseases", "Obesity"
        ]
    },
    {
        "name": "Sher-e-Bangla Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Pneumonia", "Diabetes", "Asthma", "Back pain", "Migraine"
        ]
    },
    {
        "name": "Narayanganj General Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Hypertension", "Stroke", "Heart Disease", "Obesity"
        ]
    },
    {
        "name": "Bangladesh Army Medical Corps (BAMC)",
        "type": "Public",
        "issues": [
            "Trauma", "Infections", "Cancer", "Heart Disease", "Stroke", "Mental Health Disorders", "Diabetes"
        ]
    },
    {
        "name": "Khulna Medical College Hospital",
        "type": "Public",
        "issues": [
            "Asthma", "Pneumonia", "Diabetes", "Hypertension", "Cancer", "Stroke", "Obesity", "Mental Health Disorders"
        ]
    },
    {
        "name": "Mymensingh Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Hypertension", "Diabetes", "Stroke", "Cancer", "Heart Disease", "Obesity", "Mental Health Disorders"
        ]
    },
    {
        "name": "Rajshahi Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cancer", "Stroke", "Diabetes", "Hypertension", "Asthma", "Chronic Respiratory Diseases", "Obesity"
        ]
    },
    {
        "name": "Meherpur Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Asthma", "Diabetes", "Hypertension", "Cancer", "Chronic Diseases"
        ]
    },
    {
        "name": "Cumilla Medical College Hospital",
        "type": "Public",
        "issues": [
            "Asthma", "Cold", "Flu", "Pneumonia", "Heart Disease", "Diabetes", "Hypertension"
        ]
    },
    {
        "name": "Bogra Medical College Hospital",
        "type": "Public",
        "issues": [
            "Stroke", "Heart Disease", "Cancer", "Asthma", "Pneumonia", "Diabetes", "Hypertension"
        ]
    },
    {
        "name": "Sylhet MAG Osmani Medical College Hospital",
        "type": "Public",
        "issues": [
            "Heart Disease", "Stroke", "Asthma", "Cancer", "Diabetes", "Chronic Obstructive Pulmonary Disease (COPD)"
        ]
    },
    {
        "name": "Faridpur Medical College Hospital",
        "type": "Public",
        "issues": [
            "Heart Disease", "Stroke", "Diabetes", "Hypertension", "Pneumonia", "Obesity"
        ]
    },
    {
        "name": "Bangladesh Institute of Research and Rehabilitation in Diabetes, Endocrine and Metabolic Disorders (BIRDEM)",
        "type": "Public",
        "issues": [
            "Diabetes", "Hypertension", "Obesity", "Chronic Kidney Disease", "Heart Disease"
        ]
    },
    {
        "name": "Gonoshasthaya Samajvittik Medical College & Hospital",
        "type": "Public",
        "issues": [
            "Diabetes", "Hypertension", "Heart Disease", "Stroke", "Cancer", "Asthma", "Obesity"
        ]
    },
    {
        "name": "Chandpur General Hospital",
        "type": "Public",
        "issues": [
            "Asthma", "Fever", "Cold", "Stroke", "Cancer", "Diabetes", "Obesity"
        ]
    },
    {
        "name": "Narsingdi Medical College Hospital",
        "type": "Public",
        "issues": [
            "Hypertension", "Diabetes", "Stroke", "Heart Disease", "Obesity", "Cancer", "Back pain"
        ]
    },
    {
        "name": "Noakhali Medical College Hospital",
        "type": "Public",
        "issues": [
            "Asthma", "Cancer", "Heart Disease", "Stroke", "Obesity", "Diabetes"
        ]
    },
    {
        "name": "Patuakhali Medical College Hospital",
        "type": "Public",
        "issues": [
            "Hypertension", "Stroke", "Asthma", "Diabetes", "Cancer", "Obesity", "Chronic Respiratory Diseases"
        ]
    },
    {
        "name": "Bagerhat Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cold", "Fever", "Asthma", "Stroke", "Cancer", "Hypertension", "Diabetes"
        ]
    }
])

hospital_data.extend([
    {
        "name": "Dhaka Shishu Hospital",
        "type": "Public",
        "issues": [
            "Pediatric Respiratory Infections", "Diarrhea", "Neonatal Jaundice", "Asthma", "Premature Birth", "Cystic Fibrosis"
        ]
    },
    {
        "name": "Rajshahi Orthopaedic Hospital",
        "type": "Private",
        "issues": [
            "Bone Fractures", "Spinal Disorders", "Arthritis", "Joint Pain", "Back Pain", "Orthopedic Trauma"
        ]
    },
    {
        "name": "Bangabandhu Sheikh Mujib Medical University (BSMMU)",
        "type": "Public",
        "issues": [
            "Cancer", "Heart Disease", "Diabetes", "Stroke", "Nephrology", "Obesity", "Hypertension", "Infectious Diseases"
        ]
    },
    {
        "name": "Chittagong Medical College Hospital",
        "type": "Public",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Diabetes", "Pneumonia", "Hypertension", "Asthma"
        ]
    },
    {
        "name": "Kurmitola General Hospital",
        "type": "Public",
        "issues": [
            "Stroke", "Asthma", "Diabetes", "Heart Disease", "Cancer", "Infectious Diseases", "Gastrointestinal Disorders"
        ]
    },
    {
        "name": "Bangladesh Army Medical College",
        "type": "Public",
        "issues": [
            "Cancer", "Stroke", "Diabetes", "Hypertension", "Mental Health Disorders", "Infectious Diseases"
        ]
    },
    {
        "name": "Bashundhara Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Stroke", "Pneumonia", "Asthma", "Diabetes", "Cancer", "Obesity"
        ]
    },
    {
        "name": "Kawran Bazar General Hospital",
        "type": "Private",
        "issues": [
            "Diabetes", "Asthma", "Cancer", "Hypertension", "Chronic Respiratory Diseases", "Stroke", "Pneumonia"
        ]
    },
    {
        "name": "Royal Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Cancer", "Stroke", "Chronic Obstructive Pulmonary Disease (COPD)", "Diabetes", "Asthma"
        ]
    },
    {
        "name": "United Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Diabetes", "Asthma", "Pneumonia", "Obesity"
        ]
    },
    {
        "name": "Green Life Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Stroke", "Heart Disease", "Hypertension", "Asthma", "Obesity", "Diabetes"
        ]
    },
    {
        "name": "Ibn Sina Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Pneumonia", "Asthma", "Diabetes", "Stroke", "Cancer", "Mental Health Disorders"
        ]
    },
    {
        "name": "Labaid Cardiac Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Hypertension", "Stroke", "Diabetes", "Obesity", "Cardiac Surgery"
        ]
    },
    {
        "name": "Medinova Diagnostic Center",
        "type": "Private",
        "issues": [
            "Heart Disease", "Cancer", "Obesity", "Hypertension", "Mental Health Disorders", "Stroke"
        ]
    },
    {
        "name": "Bangladesh Institute of Laser Surgery",
        "type": "Private",
        "issues": [
            "Laser Surgery", "Skin Disorders", "Eye Disorders", "Vision Problems", "Hair Removal", "Tattoo Removal"
        ]
    },
    {
        "name": "Shreepur Health Complex",
        "type": "Private",
        "issues": [
            "Diabetes", "Hypertension", "Mental Health Disorders", "Cancer", "Stroke", "Asthma"
        ]
    },
    {
        "name": "Dhanmondi Health Center",
        "type": "Private",
        "issues": [
            "Cold", "Asthma", "Cough", "Fever", "Back Pain", "Hypertension", "Diabetes"
        ]
    },
    {
        "name": "Bangladesh Eye Hospital",
        "type": "Private",
        "issues": [
            "Cataracts", "Glaucoma", "Vision Impairment", "Macular Degeneration", "Retinal Disease", "Eye Infections"
        ]
    },
    {
        "name": "Fortis Hospital Dhaka",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Diabetes", "Hypertension", "Obesity", "Pneumonia"
        ]
    },
    {
        "name": "Shahabuddin Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Stroke", "Asthma", "Diabetes", "Hypertension", "Obesity", "Heart Disease"
        ]
    },
    {
        "name": "Armed Forces Medical College",
        "type": "Public",
        "issues": [
            "Stroke", "Cancer", "Mental Health Disorders", "Cardiovascular Diseases", "Respiratory Infections"
        ]
    },
    {
        "name": "Essex Medical Center",
        "type": "Private",
        "issues": [
            "Cold", "Flu", "Asthma", "Cancer", "Hypertension", "Diabetes", "Back Pain"
        ]
    },
    {
        "name": "Royal Care Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Stroke", "Cancer", "Pneumonia", "Asthma", "Diabetes", "Hypertension"
        ]
    },
    {
        "name": "Savar General Hospital",
        "type": "Public",
        "issues": [
            "Asthma", "Diabetes", "Stroke", "Cancer", "Heart Disease", "Pneumonia", "Obesity"
        ]
    },
    {
        "name": "Medicare Hospital & Research Center",
        "type": "Private",
        "issues": [
            "Stroke", "Heart Disease", "Cancer", "Diabetes", "Hypertension", "Asthma", "Obesity"
        ]
    },
    {
        "name": "Jahurul Islam Medical College Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Stroke", "Diabetes", "Hypertension", "Mental Health Disorders", "Obesity", "Heart Disease"
        ]
    },
    {
        "name": "National Institute of Diseases of the Chest & Hospital (NIDCH)",
        "type": "Public",
        "issues": [
            "Chronic Respiratory Diseases", "Pneumonia", "Asthma", "Tuberculosis", "COPD", "Lung Cancer"
        ]
    },
    {
        "name": "General Hospital Mymensingh",
        "type": "Public",
        "issues": [
            "Cold", "Flu", "Asthma", "Diabetes", "Heart Disease", "Stroke", "Hypertension"
        ]
    },
    {
        "name": "National Orthopaedic Hospital",
        "type": "Public",
        "issues": [
            "Fractures", "Spinal Disorders", "Arthritis", "Joint Pain", "Back Pain", "Post-Surgical Rehabilitation"
        ]
    },
    {
        "name": "Shreepur General Hospital",
        "type": "Private",
        "issues": [
            "Pneumonia", "Cold", "Cough", "Asthma", "Diabetes", "Stroke", "Obesity"
        ]
    },
    {
        "name": "People's Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Diabetes", "Asthma", "Hypertension", "Obesity"
        ]
    },
    {
        "name": "Uttara Adhunik Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Stroke", "Diabetes", "Cancer", "Heart Disease", "Obesity", "Mental Health Disorders", "Respiratory Diseases"
        ]
    },
    {
        "name": "Eminent Health Care Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Hypertension", "Diabetes", "Pneumonia", "Asthma"
        ]
    },
    {
        "name": "Green Valley Hospital",
        "type": "Private",
        "issues": [
            "Cancer", "Heart Disease", "Stroke", "Obesity", "Diabetes", "Pneumonia", "Asthma"
        ]
    },
    {
        "name": "Prime Medical College & Hospital",
        "type": "Private",
        "issues": [
            "Heart Disease", "Stroke", "Asthma", "Cancer", "Diabetes", "Obesity", "Pneumonia"
        ]
    },
    {
        "name": "Dhanmondi General Hospital",
        "type": "Private",
        "issues": [
            "Stroke", "Cancer", "Heart Disease", "Hypertension", "Pneumonia", "Diabetes", "Asthma"
        ]
    }
])


# Create Hospital objects and associate them with existing Issues only
for hospital_info in hospital_data:
    # Create or get the hospital instance
    hospital, created = Hospital.objects.get_or_create(
        name=hospital_info["name"],
        type=hospital_info["type"]
    )
    
    for issue_name in hospital_info["issues"]:
        # Attempt to get an existing HealthIssue by name
        issue = HealthIssue.objects.filter(name=issue_name).first()  # Get the first matching record
        
        if issue:
            # If the issue exists, add it to the hospital's issues (many-to-many relationship)
            hospital.issues.add(issue)
        else:
            # Optionally, you can log or handle the case where the issue is not found
            print(f"Warning: Issue '{issue_name}' not found for hospital '{hospital_info['name']}'")
    
    hospital.save()
