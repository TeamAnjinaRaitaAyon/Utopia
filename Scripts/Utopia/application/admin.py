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
#entertainment/sports
admin.site.register(Sport)
admin.site.register(SportVenue)
admin.site.register(SportDate)
admin.site.register(SportSeatType)
admin.site.register(SportTickets)

#HealthCare

admin.site.register(Hospital)
admin.site.register(HealthIssue)
admin.site.register(Doctor)

#Transportation

admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Country)
