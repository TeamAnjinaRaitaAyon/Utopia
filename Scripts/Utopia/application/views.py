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
from django.template.loader import render_to_string
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

def VisitingTickets(request):
    ticket_id = request.GET.get('ticket_id')
    if request.method == 'POST':
       return redirect(HomePage)
    print(ticket_id)
    if ticket_id:
        # Retrieve the ticket using the ID from the URL
        try:
            ticket = VisitingTicket.objects.get(id=ticket_id)
        except VisitingTicket.DoesNotExist:
            ticket = None
    else:
        ticket = None

    return render(request, 'visiting_ticket.html', {'ticket': ticket})



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
    if request.method == 'POST':
        health_issue=request.POST.get('HealthIssue')
        total_price=1000
        username=UsersPrimaryDetails.objects.get(UserID=str(request.user.username))
        health_issue_name=HealthIssue.objects.get(id=health_issue)
        hospitalType = request.POST.get('HospitalType')
        hospital=request.POST.get('Hospital')
        hospital_name=Hospital.objects.get(id=hospital)
        doctor=request.POST.get('Doctor')
        doctor_name=Doctor.objects.get(id=doctor)
        visitingHour=request.POST.get('VisitingHour')
        session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
        {
            'price_data': {
                'currency': 'bdt',
                'product_data': {
                    'name': f'Patient Name : {username.UserFullName}',
                    'description': (
                        f"Health_issue: {health_issue_name}\n"
                        f"HospitalType: {hospitalType}\n"
                        f"Hospital: {hospital_name}\n"
                        f"Doctor: {doctor_name}\n"
                        f"VisitingHour: {visitingHour}"
                    ),
                },
                'unit_amount': int(total_price * 100) ,# Amount in smallest currency unit
            },
            "quantity": 1,
        },
    ],
    mode='payment',
    success_url=f"{request.build_absolute_uri('/success_healthcare/')}?session_id={{CHECKOUT_SESSION_ID}}",
    cancel_url=request.build_absolute_uri('/payment-cancelled/'),
    metadata={
        'username':(username.UserFullName),
        'total_price':(total_price),
        'health_issue_name':(health_issue_name),
        'hospital_type':(hospitalType),
        'hospital_name':(hospital_name),
        'doctor_name':(doctor_name),
        'visiting_hour':(visitingHour),
    }
    )  
        # Redirect to Stripe Checkout pa
        return redirect(session.url, code=303)
    health_issues = HealthIssue.objects.all()
    return render(request, 'Healthcare/HealthcareMain.html', {'health_issues': health_issues})
@login_required
def payment_success_healthcare(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)
    print(session.payment_status)
    
    if session.payment_status == 'paid':
        # Create the VisitingTicket object
        ticket = VisitingTicket.objects.create(
            username=session.metadata['username'],
            total_price=session.metadata['total_price'],
            health_issue_name=session.metadata['health_issue_name'],
            hospital_type=session.metadata['hospital_type'],
            hospital_name=session.metadata['hospital_name'],
            doctor_name=session.metadata['doctor_name'],
            visiting_hour=session.metadata['visiting_hour'],
        )

        # Redirect to VisitingTickets page with the ticket id in the URL
        return redirect(f'/VisitingTickets/?ticket_id={ticket.id}')
    
    return render(request, 'success.html')


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


@login_required(login_url='EntryPage')
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
                            "currency": "bdt",
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

def get_locations(request):
    city_id = request.GET.get('city')
    locations = Location.objects.filter(city_id=city_id)
    location_list = [{"id": loc.id, "name": loc.name} for loc in locations]
    return JsonResponse({"locations": location_list})

def get_destinations(request):
    location_id = request.GET.get('location')
    destinations = Destination.objects.filter(location_id=location_id).values('id', 'name')
    return JsonResponse({'destinations': list(destinations)})

def show_available_rides(request):
    if request.method == "POST":
        city_id = request.POST.get('city')
        location_id = request.POST.get('location')
        destination_id = request.POST.get('destination')
        vehicle_type = request.POST.get('vehicle')
        rides = Ride.objects.filter(
        city_id=city_id,
        location_id=location_id,
        destination_id=destination_id,
        vehicle_type=vehicle_type
    )
    if not rides:
        return JsonResponse({"error": "Sorry, Riders are not avaiable now for your location, please try again later."})
    ride_table_html = render(request, "ride_table.html", {"rides": rides, "vehicle_type": vehicle_type}).content.decode('utf-8')
    return JsonResponse({"html": ride_table_html})
    
@login_required
def get_ride_details(request):
    if request.method == 'POST':
        ride_id = request.POST.get('ride_id')
        try:
            ride = Ride.objects.get(id=ride_id)
            context = {
                'ride': ride,
                'user': request.user,
            }
            html = render_to_string('ride_details.html', context)
            return JsonResponse({'html': html})
        except Ride.DoesNotExist:
            return JsonResponse({'error': 'Invalid request'})

def ride_detail(request):
    if request.method == "POST":
        ride_id = request.POST.get('ride_id')
        ride = get_object_or_404(Ride, id=ride_id)

        html = render_to_string('ride_details.html', {
            'ride': ride,
             
        }, request=request)
        
        return JsonResponse({'html': html})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def book_ride(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ride_id = data.get('ride_id')
            ride = Ride.objects.get(id=ride_id)
            
            # Save booking in the database
            Booking.objects.create(user=request.user, ride=ride, status='confirmed')
            ride.booked = True
            ride.save()
            
            return JsonResponse({'success': True})
        except Ride.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Ride not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def CityToCity(request):
    if request.user.is_authenticated:
        return render(request, 'Transportation/CityToCity.html')
    else:
        return render(request, 'EntryPage.html')
    

def findcitytransportation(request):
        context = {}
        if request.method == 'POST':
            source_r = request.POST.get('source')
            dest_r = request.POST.get('destination')
            date_r = request.POST.get('date')
            cityride_list = CityRide.objects.filter(
                source=source_r, dest=dest_r, date=date_r)
            if cityride_list:
                return render(request, 'Transportation/citylist.html', locals())
            else:
                context["error"] = "Sorry no ride available"
                return render(request, 'Transportation/CityToCity.html', context)
        else:
            return render(request, 'Transportation/CityToCity.html')
  
# View to handle booking a ride
def citybookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('ride_id')
        seats_r = int(request.POST.get('no_seats'))
        cityride = CityRide.objects.get(id=id_r)  
        if cityride:
            if cityride.rem > int(seats_r):
                name_r = cityride.cityride_name
                cost = int(seats_r) * cityride.price
                source_r = cityride.source
                dest_r = cityride.dest
                nos_r = (cityride.nos)
                price_r = cityride.price
                date_r = cityride.date
                time_r = cityride.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = cityride.rem - seats_r
                CityRide.objects.filter(id=id_r).update(rem=rem_r)
                citybook = CityBook.objects.create(name=username_r, email=email_r, ride_name=name_r, source=source_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------citybook id-----------', citybook.id)
                # book.save()
                return render(request, 'Transportation/citybookings.html', locals())
            else:
                context["error"] = "Sorry, select fewer number of seats"
                return render(request, 'Transportation/CityToCity.html', context)

    else:
        return render(request, 'Transportation/CityToCity.html')
    
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('cityride_id')
        try:
            # Retrieve booking and corresponding cityride
            book = CityBook.objects.get(id=id_r)
            cityride = CityRide.objects.get(id=book.cityrideid)
            # Update available seats
            cityride.rem += book.nos
            cityride.save()
            # Cancel booking
            book.status = 'CANCELLED'
            book.nos = 0
            book.save()
            return redirect('seebookings')  # Redirect to the page where the user can see bookings
        except CityBook.DoesNotExist:
            context["error"] = "Booking not found"
            return render(request, 'Transportation/error.html', context)
        except CityRide.DoesNotExist:
            context["error"] = "City ride not found"
            return render(request, 'Transportation/error.html', context)
    return render(request, 'Transportation/CityToCity.html')


def seebookings(request):
    context = {}
    id_r = request.user.id
    book_list = CityBook.objects.filter(user_id=id_r) 
    if book_list.exists():
        context["book_list"] = book_list
        return render(request, 'Transportation/citybooklist.html', context)
    else:
        context["error"] = "Sorry, you have no booked rides."
        return render(request, 'Transportation/CityToCity.html', context)


def CountryToCountry(request):
    if request.user.is_authenticated:
        return render(request, 'Transportation/CountryToCountry.html')
    else:
        return render(request, 'EntryPage.html')
    

def findcountrytransportation(request):
        context = {}
        if request.method == 'POST':
            source_r = request.POST.get('source')
            dest_r = request.POST.get('destination')
            date_r = request.POST.get('date')
            countryride_list = CountryRide.objects.filter(
                source=source_r, dest=dest_r, date=date_r)
            if countryride_list:
                return render(request, 'Transportation/countrylist.html', locals())
            else:
                context["error"] = "Sorry no rides available"
                return render(request, 'Transportation/CountryToCountry.html', context)
        else:
            return render(request, 'Transportation/CountryToCountry.html')
  
# View to handle booking a ride
def countrybookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('ride_id')
        seats_r = int(request.POST.get('no_seats'))
        countryride = CountryRide.objects.get(id=id_r)  
        if countryride:
            if countryride.rem > int(seats_r):
                name_r = countryride.countryride_name
                cost = int(seats_r) * countryride.price
                source_r = countryride.source
                dest_r = countryride.dest
                nos_r = (countryride.nos)
                price_r = countryride.price
                date_r = countryride.date
                time_r = countryride.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = countryride.rem - seats_r
                CountryRide.objects.filter(id=id_r).update(rem=rem_r)
                countrybook = CountryBook.objects.create(name=username_r, email=email_r, ride_name=name_r, source=source_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------countrybook id-----------', countrybook.id)
                # countrybook.save()
                return render(request, 'Transportation/countrybookings.html', locals())
            else:
                context["error"] = "Sorry, select fewer number of seats"
                return render(request, 'Transportation/CountryToCountry.html', context)

    else:
        return render(request, 'Transportation/CountryToCountry.html')
    
def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('countryride_id')
        try:
            # Retrieve booking and corresponding cityride
            book = CountryBook.objects.get(id=id_r)
            countryride = CountryRide.objects.get(id=book.countryrideid)
            # Update available seats
            countryride.rem += book.nos
            countryride.save()
            # Cancel booking
            book.status = 'CANCELLED'
            book.nos = 0
            book.save()
            return redirect('seecountrybookings')  # Redirect to the page where the user can see bookings
        except CountryBook.DoesNotExist:
            context["error"] = "Booking not found"
            return render(request, 'Transportation/error.html', context)
        except CountryRide.DoesNotExist:
            context["error"] = "Country ride not found"
            return render(request, 'Transportation/error.html', context)
    return render(request, 'Transportation/CountryToCountry.html')

# View to show all bookings made by the user
def seecountrybookings(request):
    context = {}
    id_r = request.user.id
    book_list = CountryBook.objects.filter(user_id=id_r) 
    if book_list.exists():
        context["book_list"] = book_list
        return render(request, 'Transportation/countrybooklist.html', context)
    else:
        context["error"] = "Sorry, you have no booked rides."
        return render(request, 'Transportation/CountryToCountry.html', context)

def fetch_institutions(request, category):
    if category == 'school':
        institutions = School.objects.all().values('name', 'city', 'address', 'type')
    elif category == 'college':
        institutions = College.objects.all().values('name', 'city', 'address', 'avaiable_subject')
    elif category == 'university':
        institutions = University.objects.all().values('name', 'city', 'address', 'departments_count')
    else:
        institutions = []
        
    return JsonResponse(list(institutions), safe=False)


def Admissionn(request):
    form = AdmissionForm()

    # Handle AJAX requests for fetching related data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "GET":
        institution_type_id = request.GET.get('institution_type_id')

        if institution_type_id:
            try:
                institution_type = InstitutionType.objects.get(id=institution_type_id)

                # Fetch data based on institution type
                if institution_type.name == 'School':
                    institutions = School.objects.all()
                    classes = SchoolClass.objects.all()
                elif institution_type.name == 'College':
                    institutions = College.objects.all()
                    classes = CollegeSubject.objects.all()
                elif institution_type.name == 'University':
                    institutions = University.objects.all()
                    classes = UniversityDepartment.objects.all()
                else:
                    institutions, classes = [], []

                # Convert data to JSON format
                if institution_type.name == 'School':
                    institution_data = [{"id": inst.id, "name": inst.name} for inst in institutions]
                    class_data = [{"id": cls.id, "name": cls.class_name} for cls in classes]  # School-specific class names


                elif institution_type.name == 'College':
                    institution_data = [{"id": inst.id, "name": inst.name} for inst in institutions]
                    class_data = [{"id": cls.id, "name": cls.subject_name} for cls in classes]  # College-specific subject names
                
                elif institution_type.name == 'University':
                    institution_data = [{"id": inst.id, "name": inst.name} for inst in institutions]
                    class_data = [{"id": cls.id, "name": cls.department_name} for cls in classes]  # University-specific department names
                
                # Return JSON response
                return JsonResponse({
                    "institutions": institution_data,
                    "class_subject_department": class_data
                })

            except InstitutionType.DoesNotExist:
                return JsonResponse({"error": "Invalid Institution Type"}, status=400)

        return JsonResponse({"error": "Missing institution_type_id"}, status=400)

    # Handle form submission (POST request)
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            institution_type = form.cleaned_data['institution_type']
            institution_name = form.cleaned_data['institution_name']
            class_subject_department = form.cleaned_data['class_subject_department']
            student_name = form.cleaned_data['student_name']

            admission = Admission.objects.create(
                institution_type=institution_type,
                institution_name=institution_name,
                class_subject_department=class_subject_department,
                student_name=student_name
            )

            return redirect('thank_you')  

    # Render the form for GET request
    return render(request, 'Admission.html', {'form': form})


def ThankYou(request):
    return render(request, 'Healthcare/ThankYou.html')

def thank_you(request):
    return render(request, 'Thankyou.html')

def Thank(request):
    return render(request, 'Thank.html') 
