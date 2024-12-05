from django.contrib import admin
from application.models import *


# Register your models here.
admin.site.register(UsersPrimaryDetails)
admin.site.register(PoliticiansPrimaryDetails)
admin.site.register(CountryConstituency)
admin.site.register(MPElection)
admin.site.register(MinisterPrimaryDetails)
admin.site.register(CountryMinistries)
admin.site.register(PublicOpinions)
#entertainment
admin.site.register(SportsEvent)
admin.site.register(Ticket)

#HealthCare
admin.site.register(VisitingTicket)
admin.site.register(Hospital)
admin.site.register(HealthIssue)
admin.site.register(Doctor)

#Transportation
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Country)
admin.site.register(Ride)
admin.site.register(Destination)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(CityRide)
admin.site.register(CityBook)
admin.site.register(UserCity)
admin.site.register(CountryRide)
admin.site.register(CountryBook)
admin.site.register(UserCountry)

admin.site.register(University)
admin.site.register(College)
admin.site.register(School)