import random
import requests
import datetime
import calendar
import re
from .utils import send_email_to_client
from bs4 import BeautifulSoup
from newsapi.newsapi_client import NewsApiClient
from django.utils.html import strip_tags
from django.urls import reverse
from django.conf import Settings
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib import messages
from django.db.models import Q
from .forms import *
from application.models import *
from django.contrib.auth.decorators import login_required
from itertools import chain
import os
import json
import pytz
import datetime
from datetime import date


# Create your views here.

def WelcomePage(request):
    return render(request, 'WelcomePage.html')

@login_required(login_url='EntryPage')
def ServicePage(request):
    return render(request, 'ServicePage.html')

def EntryPage(request):
    if request.method == 'POST':
        name = request.POST.get('button_name')
        if name == 'signup':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            form = RegisterForm(request.POST)
            if form.is_valid():
                my_usr = User.objects.create_user(
                    username, email, password)
                my_usr.save()
                user = authenticate(request, username=username,
                                    password=password, email=email)
                login(request, user)
                return redirect('RegistrationFormPage')
        elif name == 'login':
            username = request.POST.get('username')
            password = request.POST.get('pswd')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HomePage)
            else:
                messages.error(
                    request, ' The username or password you entered is incorrect')
        elif name == 'Guest':
            username = '1234'
            email = '1234@uap-bd.edu'
            password = 'AYONGHOSHAJOYGHOSH'
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HomePage)
    request.session.clear()
    return render(request, 'EntryPage.html')


@login_required
def RegistrationFormPage(request):
    if request.method == 'POST':
        UserID = request.user.username
        UserEmail = request.user.email
        UserFullName = request.POST.get('full_name')
        UserGender = request.POST.get('gender')
        UserOccupation = request.POST.get('occupation')
        UserDateOfBirth = request.POST.get('date_of_birth')
        UserMobileNum = request.POST.get('mobile_number')
        UserPoints = 1000
        UserImageFilename = request.FILES.get('image')
        UserRole = request.POST.get('role')
        name = request.POST.get('save')
        birthday = date.fromisoformat(UserDateOfBirth)
        today = date.today()
        UserAge = today.year - birthday.year - \
            ((today.month, today.day) < (birthday.month, birthday.day))
        if UserImageFilename:
            UserImageFilename.name = f'{UserID}.jpg'
            with open(f'media', 'wb') as f:
                f.write(UserImageFilename.read())
        if name == 'confirm':
            user_details = UsersPrimaryDetails(UserID, UserEmail, UserFullName, UserGender, UserOccupation,
                                               UserDateOfBirth, UserRole, UserMobileNum, UserPoints, UserImageFilename, UserAge)
            user_details.save()
            userocp = str(UserOccupation)
            if userocp.__contains__("Politician"):
                print(UserID)
                politician_details = PoliticiansPrimaryDetails(
                    UserID, UserRole, UserFullName, 0, 0, 0, UserID, False, False)
                politician_details.save()
            return redirect(HomePage)
    return render(request, 'RegistrationFormPage.html')

@login_required(login_url='EntryPage')
def HomePage(request):
    UserID = request.user.username
    user = UsersPrimaryDetails.objects.get(UserID=UserID)
    host = user.UserImageFilename.url
    host = "http://127.0.0.1:8000/"+host
    context = {
        'user': user,
    }
    return render(request, 'HomePage.html', context)


@login_required
def VotingPage(request):
    if request.method == 'POST':
        UserID = request.user.username
        vote_setup = request.POST.get('save')
        now = datetime.datetime.now(pytz.timezone('UTC'))
        if vote_setup == 'setup':
            return redirect(ElectionSetupPage)
        Election = MPElection.objects.filter(EndTime__gte=now)
        for voteo in Election:
            one = json.loads(voteo.VoteDoneList)
            if str(UserID) not in one:
                if vote_setup == 'Cd1v':
                    voteo.Candidate1Vote += 1
                    one += str(UserID)
                    one = json.dumps(one, separators=(",", ","))
                    voteo.VoteDoneList = one
                if vote_setup == 'Cd2v':
                    voteo.Candidate2Vote += 1
                    one += str(UserID)
                    one = json.dumps(one, separators=(",", ","))
                    voteo.VoteDoneList = one
                voteo.save()
            else:
                messages.error(
                    request, 'You have already voted in this election.')
    timenow = datetime.datetime.now(pytz.timezone('UTC'))
    voting = MPElection.objects.filter(EndTime__lte=timenow)
    elc = MPElection.objects.filter(EndTime__gte=timenow)
    check = elc.exists()
    userid = int(request.user.username)
    ss = 00000000
    vc1 = 1
    vc2 = 1
    for vote in voting:
        vote.ElectionStatus = False
        vote.save()
        vc1 = 1
        vc2 = 1
    for vote in elc:
        vc1 = vote.Candidate1Vote
        vc2 = vote.Candidate2Vote
        vc3 = vc1+vc2
        if vc3 != 0:
            vc1 = vc1*100/vc3

            vc2 = vc2*100/vc3
            vc1 = round(vc1, 2)
            vc2 = round(vc2, 2)
    context = {
        'Elections': elc,
        'UserID': userid,
        'Check': check,
        'President': ss,
        'vc1': vc1,
        'vc2': vc2,
    }
    return render(request, 'VotingPage.html', context)


@login_required(login_url='EntryPage')
def MinistryPage(request):
    if request.method == 'POST':
        minister_setup = request.POST.get('save')
        if minister_setup == 'setup':
            return redirect(MinistrySetupPage)
    UserID = int(request.user.username)
    objMinisterList = CountryMinistries.objects.exclude(MinisterName='1')
    ministerids = []
    for mid in objMinisterList:
        ministerids.append(mid.MinisterID)
    objUserPrimaryDetails = []
    objMinisterPrimaryDetails = []
    for id in ministerids:
        objUserPrimaryDetails += (UsersPrimaryDetails.objects.filter(UserID=id))
        objUserPrimaryDetails = list(objUserPrimaryDetails)
        objMinisterPrimaryDetails += (
            MinisterPrimaryDetails.objects.filter(MinisterNumberID=id))
        objMinisterPrimaryDetails = list(objMinisterPrimaryDetails)
    ss = 00000000
    context = {
        'UserID': UserID,
        'President': ss,
        'MinisterList': objMinisterPrimaryDetails,
        'MinisterDetails': objUserPrimaryDetails,
    }
    return render(request, 'MinistryPage.html', context)


@login_required(login_url='EntryPage')
def ElectionSetupPage(request):
    if request.method == 'POST':
        Candidate1 = request.POST.get('Candidate1')
        Candidate2 = request.POST.get('Candidate2')
        Constituency = request.POST.get('Constituency')
        name = request.POST.get('save')
        Cd1 = int(Candidate1)
        Cd2 = int(Candidate2)
        findCandidate = PoliticiansPrimaryDetails.objects.filter(
            PoliticianID=Cd1)
        findCandidate1 = findCandidate.exists()
        findCandidate = PoliticiansPrimaryDetails.objects.filter(
            PoliticianID=Cd2)
        findCandidate2 = findCandidate.exists()
        findconstituency = CountryConstituency.objects.filter(
            ConstituencyName=Constituency)
        findconstituency0 = findconstituency.exists()
        print(findconstituency0, findCandidate1, findCandidate2)
        if (findCandidate1 is False or findCandidate2 is False or findconstituency0 is False):
            messages.error(
                request, 'could not find any matches for your input')
        elif Cd1 == Cd2:
            messages.error(
                request, 'Please select two different candidates.')
        else:
            time = datetime.datetime.now(pytz.timezone('UTC'))
            starttime = time
            time = increase_hour(time)
            endtime = time
            votedonelist = json.dumps("", separators=(",", ","))
            if name == "confirm":
                Election = MPElection(Candidate1, Candidate2,
                                      0, 0, True, starttime, endtime, Constituency, Cd1, Cd2, votedonelist)
                Election.save()
            return redirect(VotingPage)
    AfterElection = MPElection.objects.filter(ElectionStatus=False)
    for Ae in AfterElection:
        Constituency = Ae.Constituency
        Ca1 = Ae.Candidate1Vote
        Ca2 = Ae.Candidate2Vote
        Cd1 = Ae.Cd1
        Cd2 = Ae.Cd2
        if Ca1 > Ca2:
            WinnerID = Cd1
        elif Ca1 < Ca2:
            WinnerID = Cd2
        else:
            WinnerID = -800
            AePPd1 = PoliticiansPrimaryDetails.objects.get(Pid=Ae.Cd1)
            AePPd2 = PoliticiansPrimaryDetails.objects.get(Pid=Ae.Cd2)
            AePPd1.ElectionRun += 1
            AePPd2.ElectionRun += 1
            AePPd1.save()
            AePPd2.save()
        if Cd1 < Cd2 or Cd1 > Cd2:
            AePPd = PoliticiansPrimaryDetails.objects.get(Pid=WinnerID)
            AePPd.TimeLeft = 1
            AePPd.ElectionRun += 1
            AePPd.ElectionWon += 1
            AePPd.PoliticianRole = f'MP({Constituency})'
            AePPd.IsMP = True
            AePPd.save()
            AeUpd = UsersPrimaryDetails.objects.get(UserID=WinnerID)
            AeUpd.UserRole = f'MP({Constituency})'
            AeUpd.UserPoints += 1000
            AeUpd.save()
            obj_constituency = CountryConstituency.objects.get(
                ConstituencyName=Constituency)
            obj_constituency.TimeLeft = 1
            obj_constituency.save()
            Ae.ElectionStatus = True
            Ae.save()
    ConstituencyList = CountryConstituency.objects.filter(TimeLeft='0')
    PoliticiansList = PoliticiansPrimaryDetails.objects.filter(TimeLeft='0')
    context = {}
    context.update({"ConstituencyList": ConstituencyList})
    context.update({"PoliticiansList": PoliticiansList})
    return render(request, 'ElectionSetupPage.html', context)


@login_required(login_url='EntryPage')
def MinistrySetupPage(request):
    if request.method == 'POST':
        MinistryName = request.POST.get('Ministry')
        MinisterName = request.POST.get('MP')
        name = request.POST.get('save')
        MinisterID = get_number_from_string(MinisterName)
        MinisterName = get_text_from_string(MinisterName)
        if name == 'confirm':
            ObjCountryMinistry = CountryMinistries.objects.get(
                MinistryName=MinistryName)
            ObjCountryMinistry.MinisterName = MinisterName
            ObjCountryMinistry.MinisterID = MinisterID
            objPoliticianPrimaryDetails = PoliticiansPrimaryDetails.objects.get(
                PoliticianID=MinisterID)
            objPoliticianPrimaryDetails.IsMinister = True
            tmpConstitutionName = extract_district_from_mp(
                objPoliticianPrimaryDetails.PoliticianRole)
            objMinisterPrimaryDetails = MinisterPrimaryDetails(
                MinistryName, MinisterID, tmpConstitutionName, MinisterID)
            objMinisterPrimaryDetails.save()
            objPoliticianPrimaryDetails.save()
            ObjCountryMinistry.save()
            return redirect(MinistryPage)

    PoliticiansList = PoliticiansPrimaryDetails.objects.filter(
        Q(IsMP=True) & Q(IsMinister=False))
    MinistriesList = CountryMinistries.objects.filter(MinisterName='1')
    context = {}
    context.update({"MpList": PoliticiansList})
    context.update({'MinistryList': MinistriesList})
    return render(request, 'MinistrySetupPage.html', context)

#transportation
@login_required(login_url='EntryPage')
def TransportationMain(request):
    return render(request, 'Transportation/TransportationMain.html')

@login_required(login_url='EntryPage')
def InCity(request):
    CityList = City.objects.all()
    context = {}
    context.update({"CityList": CityList})
    return render(request, 'Transportation/InCity.html',context)

@login_required(login_url='EntryPage')
def CityToCity(request):
    return render(request, 'Transportation/CityToCity.html')

@login_required(login_url='EntryPage')
def CountryToCountry(request):
    return render(request, 'Transportation/CountryToCountry.html')


def get_Location(request):
    city = request.GET.get('city')
    request.session['city']=city
    locations = Neighborhood.objects.filter(
        city=city
    )  
    location_data= [
        {"name": location.name,'id':location.id}
        for location in locations
    ]

    return JsonResponse({"location":location_data})


def get_Destination(request):
    location = request.GET.get('location')
    if location is not None:
        try:
            location = int(location)  # Ensure location is an integer
        except ValueError:
            return JsonResponse({"error": "Invalid location ID"}, status=400)
    
    city = request.session.get('city', [])
    print(location, city)
    
    destinations = Neighborhood.objects.filter(city=city)
    print(destinations)
    
    destination_data = [
        {"name": destination.name, 'id': destination.id}
        for destination in destinations if destination.id != location
    ]
    
    print(f"this is {destination_data}")
    return JsonResponse({"destination": destination_data})

def get_Price(request):
    return 
def Clinic(request):
    return render(request, "Healthcare/Category.html/Clinic.html")


def Hospital(request):
    return render(request, "Healthcare/Category.html/Hospital.html")


def Pharmacy(request):
    return render(request, "Healthcare/Category.html/Pharmacy.html")


def Diagnostic(request):
    return render(request, "Healthcare/Category.html/Diagnostic.html")


def Eyeclinic(request):
    return render(request, "Healthcare/Category.html/Eyeclinic.html")


def PublicClinic(request):
    return render(request, "Healthcare/Clinic.html/PublicClinic.html")


def PrivateClinic(request):
    return render(request, "Healthcare/Clinic.html/PrivateClinic.html")


def PublicHospital(request):
    return render(request, "Healthcare/Hospital.html/PublicHospital.html")


def PrivateHospital(request):
    return render(request, "Healthcare/Hospital.html/PrivateHospital.html")


def PrivateDiagnostic(request):
    return render(request, "Healthcare/Diagnostic.html/PrivateDiagnostic.html")


def PublicDiagnostic(request):
    return render(request, "Healthcare/Diagnostic.html/PublicDiagnostic.html")


def PrivateEyeclinic(request):
    return render(request, "Healthcare/Eyeclinic.html/PrivateEyeclinic.html")


def PublicEyeclinic(request):
    return render(request, "Healthcare/Eyeclinic.html/PublicEyeclinic.html")


def HospitalAppointmentPage(request):
    return render(request, "Healthcare/Hospital.html/HospitalAppointmentPage.html")


def PharmacyBookingPage(request):
    return render(request, "Healthcare/Pharmacy.html/PharmacyBookingPage.html")


def DiagnosticAppointmentPage(request):
    return render(request, "Healthcare/Diagnostic.html/DiagnosticAppointmentPage.html")


def ClinicAppointmentPage(request):
    return render(request, "Healthcare/Clinic.html/ClinicAppointmentPage.html")


def EyeclinicAppointmentPage(request):
    return render(request, "Healthcare/Eyeclinic.html/EyeclinicAppointmentPage.html")


def ThankYou(request):
    return render(request, 'Healthcare/ThankYou.html')


@login_required
def EducationPage(request):
    return render(request, 'EducationPage.html')



def success(request):
    return render(request, 'Education/success.html')


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SportsEvent

@login_required
def EntertainmentPage(request):
    sportsEvent = SportsEvent.objects.all()
    return render(request, 'EntertainmentPage.html', {'sportsEvent': sportsEvent})


import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.conf import settings
from .models import SportsEvent, Ticket
import json

# Set up Stripe API key
stripe.api_key = settings.STRIPE_TEST_API_KEY
@login_required
def event_details(request, event_id):
    event = get_object_or_404(SportsEvent, pk=event_id)

    if request.method == 'POST':
        # Get the selected seats and total price from the POST data
        selected_seats = json.loads(request.POST.get('selectedSeats', '[]'))
        total_price = float(request.POST.get('totalPrice', 0.0))
        # Create a Stripe Checkout session
        session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[
        {
            'price_data': {
                'currency': 'bdt',
                'product_data': {
                    'name': f'{event.event_name} Tickets',
                    'description': (
                        f"Event: {event.event_name}\n"
                        f"Match: {event.match_details}\n"
                        f"Sport: {event.sport_type}\n"
                        f"Date: {event.event_date.strftime('%d %b %Y, %I:%M %p')}\n"
                        f"Venue: {event.venue}, {event.city}, {event.country}"
                    ),
                },
                'unit_amount': int(total_price/len(selected_seats) * 100) ,  # Amount in smallest currency unit
            },
            'quantity': len(selected_seats),
        },
    ],
    mode='payment',
    success_url=f"{request.build_absolute_uri('/success/')}?session_id={{CHECKOUT_SESSION_ID}}",
    cancel_url=request.build_absolute_uri('/payment-cancelled/'),
    client_reference_id=str(event.id),
    metadata={
        'selected_seats': ','.join(selected_seats),
    }
)
        # Redirect to Stripe Checkout pa
        return redirect(session.url, code=303)

    return render(request, 'event_details.html', {'event': event}) 

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
import stripe
from django.conf import settings
from .models import SportsEvent, Ticket

# Set the Stripe API key
stripe.api_key = settings.STRIPE_TEST_API_KEY

@login_required
def payment_success(request):

    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    print(session.payment_status)
    if session.payment_status == 'paid':
        # Retrieve the event using client_reference_id
        event = get_object_or_404(SportsEvent, pk=session.client_reference_id)
        
        # Extract metadata from the session
        selected_seats = session.metadata['selected_seats'].split(',')
        total_price = float(session.amount_total) / 100  # Convert cents to currency unit
        
        # Validate and update seat availability
        for seat in selected_seats:
            if seat in event.seats and event.seats[seat].get('available', False):
                event.seats[seat]['available'] = False  # Mark seat as unavailable
            else:
                return render(request, 'payment_failure.html', {'message': 'Some seats are already booked.'})
        
        # Save updated event seat availability
        event.save()

        # Create tickets
        tickets = []
        for seat in selected_seats:
            ticket = Ticket.objects.create(
                user=request.user,
                event_name=event.event_name,
                match_details=event.match_details,
                sport_type=event.sport_type,
                event_date=event.event_date,
                venue=event.venue,
                city=event.city,
                country=event.country,
                event_image=event.event_image,
                seats=event.seats,  # Include the updated seat information
                selected_seats=[seat],  # Include the specific selected seat
                total_price=total_price / len(selected_seats),  # Calculate price per seat
                purchase_date=now(),  # Use the current timestamp
            )
            tickets.append(ticket)

        # Redirect to the SportTicket page with ticket IDs
        ticket_ids = [ticket.id for ticket in tickets]
        return redirect(f'/SportTicket/?ticket_ids={",".join(map(str, ticket_ids))}')
    
    return render(request, 'success.html')




@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = 'your-stripe-webhook-secret'
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return JsonResponse({'success': False}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'success': False}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Handle successful payment and create tickets here
        # Example: session['metadata'] can store event_id or user info

    return JsonResponse({'success': True})



from django.shortcuts import render, get_object_or_404
from .models import Ticket

def SportTicket(request):
    # Get the list of ticket IDs from the query parameters
    ticket_ids = request.GET.get('ticket_ids', '')
    print(f'this is {ticket_ids}')
    if request.method == 'POST':
       return redirect(TicketsPage)
    if ticket_ids:
        # Convert the ticket_ids into a list of integers
        ticket_ids_list = list(map(int, ticket_ids.split(',')))

        # Fetch the tickets based on the IDs
        tickets = Ticket.objects.filter(id__in=ticket_ids_list, user=request.user)

        # Check if tickets exist, otherwise handle the case
        if not tickets:
            return redirect('some_error_or_homepage_url')  # Redirect if no tickets found for the user
    else:
        tickets = []

    # Render the template with the tickets
    return render(request, 'SportTicket.html', {'tickets': tickets})


# sports finish

#HealthCare Start 
from .models import HealthIssue
@login_required(login_url='EntryPage')
def HealthcareMain(request):
    health_issues = HealthIssue.objects.all()
    return render(request, 'Healthcare/HealthcareMain.html', {'health_issues': health_issues})
from django.http import JsonResponse
from .models import HealthIssue, Hospital, Doctor

def get_hospitals(request):
    health_issue_id = request.GET.get('health_issue')
    hospital_type = request.GET.get('hospital_type')
    print(f'this is {health_issue_id,hospital_type}')

    hospitals = Hospital.objects.filter(
        issues__id=health_issue_id, type=hospital_type
    )

    hospital_data = [
        {"id": hospital.id, "name": hospital.name}
        for hospital in hospitals
    ]
    
    return JsonResponse({"hospitals": hospital_data})

from django.http import JsonResponse
from .models import HealthIssue, Hospital, Doctor

from django.http import JsonResponse
from .models import Doctor

def get_doctors(request):
    # Get health_issue_id and hospital_id from the GET request
    health_issue_id = request.GET.get('health_issue')
    hospital_id = request.GET.get('hospital')
    
    # Print for debugging
    print(f"Health Issue ID: {health_issue_id}, Hospital ID: {hospital_id}")

    # Fetch doctors who are associated with the selected hospital and health issue
    doctors = Doctor.objects.filter(
        hospitals__id=hospital_id,  # Filter by hospital
        health_issue__id=health_issue_id  # Filter by health issue
    )

    # Prepare a list of doctor names and ids to return as JSON
    doctor_data = [
        {"id": doctor.id, "name": doctor.name}  # Send doctor ID and name
        for doctor in doctors
    ]
    print(doctor_data)
    # Return a JSON response containing the doctor data
    return JsonResponse({"doctors": doctor_data})

from django.http import JsonResponse
from .models import Doctor

from django.http import JsonResponse
from .models import Doctor

def get_visiting_hours(request):
    doctor_id = request.GET.get('doctor')

    # Get the doctor object by ID
    doctor = Doctor.objects.get(id=doctor_id)

    # Format the visiting hours in a human-readable way
    formatted_visiting_hours = []
    for entry in doctor.visiting_hours:
        day = entry.get("day", "Unknown Day")
        hours = entry.get("hours", "No Hours Available")
        formatted_visiting_hours.append(f"{day}: {hours}")

    # Return the formatted visiting hours in the response
    return JsonResponse({"visiting_hours": formatted_visiting_hours})



#healthCare Finish


@login_required
def Am_I_A_CitizenPage(request):
    if request.method == 'POST':
        news = request.POST.get('save')
        if news == "confirm":
            userOpinion = request.POST.get('Opinions')
            opinion = PublicOpinions(request.user.username, userOpinion)
            opinion.save()
        else:
            return redirect(NewsDetailsPage, news)
    opinions = PublicOpinions.objects.all()

    api_key = '392d7f4dc8c84340adfd4248a825e0e5'
    newsapi = NewsApiClient(api_key=api_key)

    # Specify your query parameters
    query_params = {
        'language': 'en',  # Language code (e.g., 'en' for English)
    }

    # Fetch news articles using the `get_top_headlines` method
    headlines = newsapi.get_top_headlines(**query_params)
    headlines = headlines['articles'][:10]
    context = {
        'NEWS': headlines,
        'PublicOpinion': opinions
    }
    return render(request, 'Am-I-A-CitizenPage.html', context)


@login_required
def NewsDetailsPage(request, news):
    response = requests.get(news)
    html_content = response.content

#   Remove any unnecessary elements from the HTML content.
    soup = BeautifulSoup(html_content, "html.parser")
    header = soup.find("header")
    footer = soup.find("footer")
    nav = soup.find("nav")
    if header is not None:
        header.extract()
    if footer is not None:
        footer.extract()
    if nav is not None:
        nav.extract()
    context = {
        "news": soup.prettify()
    }
    return render(request, 'NewsDetailsPage.html', context)

def AboutPage(request):
    return render(request, 'AboutPage.html')


@login_required
def ContactPage(request):
    return render(request, 'ContactPage.html')

def HelpPage(request):
    return render(request, 'HelpPage.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def TicketsPage(request):
    # Extract the username of the logged-in user
    username = request.user.username  # Extracting just the username

    # Filter the tickets based on the logged-in user's username
    tickets = Ticket.objects.filter(user__username=username)  # Filtering tickets by username

    # Print the username for debugging (optional)
    print(f"Logged-in User's Username: {username}")
    
    return render(request, 'TicketsPage.html', {'Tickets': tickets})


#payment
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_page(request):
    return render(request, "payments/payment_page.html", {"publishable_key": settings.STRIPE_PUBLISHABLE_KEY})

def payment_cancel(request):
    return render(request,"payments/cancel.html")
def create_checkout_session(request):
    if request.method == "POST":
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {"name": "Example Product"},
                            "unit_amount": 2000,  # $20.00 in cents
                        },
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url="http://127.0.0.1:8000/success/",
                cancel_url="http://127.0.0.1:8000/cancel/",
            )
            return JsonResponse({"id": session.id})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        
        

def Undefine(request, undefined_path):
    return redirect(HomePage)
