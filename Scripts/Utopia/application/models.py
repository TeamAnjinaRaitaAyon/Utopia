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


# entertainment/Sports


class Sport(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SportVenue(models.Model):
    Sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class SportDate(models.Model):
    SportVenue = models.ForeignKey(SportVenue, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SportSeatType(models.Model):
    SportDate = models.ForeignKey(SportDate, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SportTickets(models.Model):
    SportName = models.CharField(max_length=500)
    SportVenue = models.CharField(max_length=1000)
    SportDate = models.CharField(max_length=100)
    SportSeatType = models.CharField(max_length=100)
    SportSeatNumber = models.CharField(max_length=500)
    SportTicketPrice = models.CharField(max_length=500)
    UserID = models.ForeignKey(UsersPrimaryDetails, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)


from django.core.exceptions import ValidationError  # Import Vali

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
