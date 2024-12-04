from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete


class UsersPrimaryDetails(models.Model):
    UserID = models.IntegerField(primary_key=True)
    UserEmail = models.EmailField(max_length=254)
    UserFullName = models.CharField(max_length=255)
    UserGender = models.CharField(max_length=255)
    UserOccupation = models.CharField(max_length=255)
    UserDateOfBirth = models.DateField()
    UserRole = models.CharField(max_length=255)
    UserMobileNum = models.CharField(max_length=255)
    UserPoints = models.IntegerField()
    UserImageFilename = models.ImageField()
    UserAge = models.IntegerField()

    def __str__(self):
        return str(self.UserID)


class PoliticiansPrimaryDetails(models.Model):
    PoliticianID = models.OneToOneField(
        UsersPrimaryDetails, on_delete=models.CASCADE, primary_key=True)
    PoliticianRole = models.CharField(max_length=255)
    PoliticianName = models.CharField(max_length=256)
    TimeLeft = models.IntegerField()
    ElectionRun = models.IntegerField()
    ElectionWon = models.IntegerField()
    Pid = models.IntegerField()
    IsMP = models.BooleanField()
    IsMinister = models.BooleanField()

    def __str__(self):
        return str(self.PoliticianName)


class CountryConstituency(models.Model):
    ConstituencyName = models.CharField(max_length=255)
    TimeLeft = models.IntegerField()

    def __str__(self):
        return str(self.ConstituencyName)


class MPElection(models.Model):
    Candidate1ID = models.ForeignKey(
        UsersPrimaryDetails, on_delete=models.CASCADE, related_name="Candidate1ID")
    Candidate2ID = models.ForeignKey(
        UsersPrimaryDetails, on_delete=models.CASCADE, related_name="Candidate2ID")
    Candidate1Vote = models.IntegerField()
    Candidate2Vote = models.IntegerField()
    ElectionStatus = models.BooleanField()
    StartTime = models.DateTimeField(primary_key=True)
    EndTime = models.DateTimeField()
    Constituency = models.CharField(max_length=254)
    Cd1 = models.IntegerField()
    Cd2 = models.IntegerField()
    VoteDoneList = models.JSONField()

    def __str__(self):
        return str(self.StartTime)


class CountryMinistries(models.Model):
    MinistryName = models.CharField(max_length=300, primary_key=True)
    MinisterName = models.CharField(max_length=255)
    MinisterID = models.IntegerField()

    def __str__(self):
        return str(self.MinistryName)


class MinisterPrimaryDetails(models.Model):
    MinistryName = models.OneToOneField(
        CountryMinistries, on_delete=models.CASCADE)
    MinisterID = models.OneToOneField(
        PoliticiansPrimaryDetails, on_delete=models.CASCADE, primary_key=True)
    MinisterConstituency = models.CharField(max_length=254)
    MinisterNumberID = models.IntegerField()

    def __str__(self):
        return str(self.MinisterID)


class PublicOpinions(models.Model):
    UserID = models.IntegerField()
    Opinion = models.TextField(primary_key=True)

    def __str__(self):
        return str(self.Opinion)


# entertainment

class SportsEvent(models.Model):
    event_name = models.CharField(max_length=255)  # Event name, e.g., "World Cup Final"
    match_details = models.CharField(max_length=255, blank=True, null=True)  # Teams playing, e.g., "Bangladesh vs. India"
    sport_type = models.CharField(max_length=100)  # Type of sport, e.g., "Cricket"
    event_date = models.DateTimeField()  # Date and time of the event
    venue = models.CharField(max_length=255)  # Venue name
    city = models.CharField(max_length=100)  # City where the event is happening
    country = models.CharField(max_length=100)  # Country where the event is happening
    event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Optional event image
    seats = models.JSONField(default=dict)  # Dictionary to store seat details

    def __str__(self):
        return f"{self.event_name} - {self.match_details or 'Details Not Provided'}"


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user purchasing the ticket
    event_name = models.CharField(max_length=255)  # Event name, e.g., "World Cup Final"
    match_details = models.CharField(max_length=255, blank=True, null=True)  # Teams playing, e.g., "Bangladesh vs. India"
    sport_type = models.CharField(max_length=100)  # Type of sport, e.g., "Cricket"
    event_date = models.DateTimeField()  # Date and time of the event
    venue = models.CharField(max_length=255)  # Venue name
    city = models.CharField(max_length=100)  # City where the event is happening
    country = models.CharField(max_length=100)  # Country where the event is happening
    event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Optional event image
    seats = models.JSONField(default=dict)  # Dictionary to store seat details
    selected_seats = models.JSONField()  # List of selected seats
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for the tickets
    purchase_date = models.DateTimeField(default=timezone.now)  # Timestamp of the ticket purchase

    def __str__(self):
        return f"Ticket for {self.event_name} - {self.user.username}"




from django.core.exceptions import ValidationError  # Import Vali

from django.db import models

# Assuming these are your models:
# UsersPrimaryDetails, HealthIssue, Hospital, Doctor

from django.db import models
import random
import string

# Function to generate a custom ticket ID (unique and random)
def generate_ticket_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

class VisitingTicket(models.Model):
    # Create ticket_id as CharField and make it unique
    ticket_id = models.CharField(max_length=10, unique=True, editable=False)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price for the visit
    username = models.CharField(max_length=255)  # Store the username directly as a string
    health_issue_name = models.CharField(max_length=255)  # Store health issue name as a string
    hospital_type = models.CharField(max_length=50)  # Type of hospital (Public/Private)
    hospital_name = models.CharField(max_length=255)  # Store hospital name as a string
    doctor_name = models.CharField(max_length=255)  # Store doctor name as a string
    visiting_hour = models.CharField(max_length=50)  # Store the selected visiting hour (e.g., "10:00 AM")

    # Overriding the save method to auto-generate the ticket_id
    def save(self, *args, **kwargs):
        if not self.ticket_id:  # Only generate ticket_id if it isn't already set
            self.ticket_id = generate_ticket_id()  # Assign generated ticket ID
        super().save(*args, **kwargs)  # Call the parent save method to save the object

    def __str__(self):
        return f"Ticket ID: {self.ticket_id} for {self.username} - {self.health_issue_name}"



class HealthIssue(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    PUBLIC = 'Public'
    PRIVATE = 'Private'
    HOSPITAL_TYPE_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    type = models.CharField(
        max_length=10,
        choices=HOSPITAL_TYPE_CHOICES,
        default=PUBLIC,
    )
    
    # List of issues that can be cured or solved in the hospital
    issues = models.ManyToManyField(HealthIssue, blank=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    health_issue = models.ForeignKey(HealthIssue, on_delete=models.CASCADE)
    hospitals = models.ManyToManyField(Hospital)
    
    # Visiting hours for the doctor, in a list (could be JSON or a more detailed format as required)
    visiting_hours = models.JSONField(default=list)  # JSON format for storing visiting hours (list of dicts)

    def __str__(self):
        return self.name

    def clean(self):
        # Check if the health_issue exists in the database
        if self.health_issue and not HealthIssue.objects.filter(id=self.health_issue.id).exists():
            raise ValidationError("The HealthIssue assigned does not exist in the database.")

    def save(self, *args, **kwargs):
        # Ensure the health_issue is valid before saving
        self.clean()
        super().save(*args, **kwargs)  # Call the parent save method


#Transportation

# models.py


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='neighborhoods', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city.name})"
