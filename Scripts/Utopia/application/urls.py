from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EntryPage/', views.EntryPage, name='EntryPage'),
    path('RegistrationFormPage/',views.RegistrationFormPage,name='RegistrationFormPage'),
    path('',views.WelcomePage, name='WelcomePage'),
    path('ServicePage/',views.ServicePage, name='ServicePage'),
    path('NewsDetailsPage/',views.NewsDetailsPage, name='NewsDetailsPage'),
    path('HomePage',views.HomePage, name='HomePage'),
    path('VotingPage/',views.VotingPage,name='VotingPage'),
    path('ElectionSetupPage/',views.ElectionSetupPage,name='ElectionSetupPage'),
    path('MinistryPage/',views.MinistryPage,name='MinistryPage'),
    path('MinistySetupPage/',views.MinistrySetupPage,name='MinistrySetupPage'),

    path('EducationPage',views.EducationPage,name='EducationPage'),
    
    
    path('EntertainmentPage/',views.EntertainmentPage,name='EntertainmentPage'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),
    
    
    
    path('Am_I_A_Citizen/',views.Am_I_A_CitizenPage,name='Am_I_A_CitizenPage'),
    path('NewsDetailsPage/<path:news>/',views.NewsDetailsPage, name='NewsDetailsPage'),
    path('AboutPage/',views.AboutPage,name='AboutPage'),
    path('ContactPage/',views.ContactPage,name='ContactPage'),
    path('HelpPage/',views.HelpPage,name='HelpPage'),
    path('TicketsPage/',views.TicketsPage,name='TicketsPage'),
   path('SportTicket/',views.SportTicket,name='SportTicket'),
    path('TransportationMain/', views.TransportationMain, name='TransportationMain'),
    path('InCity/', views.InCity, name='InCity'),
    path('CityToCity/', views.CityToCity, name='CityToCity'),
    path('CountryToCountry/', views.CountryToCountry, name='CountryToCountry'),
    path('get_locations/', views.get_Location, name='get_locations'),
    path('get_destination/', views.get_Destination, name='get_destination'),
    path('get_price/', views.get_Price, name='get_price'),

    


    

    path('HealthcareMain',views.HealthcareMain,name='HealthcareMain'),
    path('get_hospitals/', views.get_hospitals, name='get_hospitals'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_visiting_hours/', views.get_visiting_hours, name='get_visiting_hours'),
    
    
    path('ThankYou', views.ThankYou, name='ThankYou'),

    path('<path:undefined_path>/', views.Undefine),
    
    
    #payment
    
    path("payment-page/", views.payment_page, name="payment_page"),
    path("create-checkout-session/", views.create_checkout_session, name="create_checkout_session"),
    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
