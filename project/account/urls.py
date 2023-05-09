from django.urls import path
from . import api
app_name='account'
urlpatterns = [
    #create account
    path('register-ph/', api.PharmacyRegistration.as_view(), name='Register-Pharmacy'),
    path('register-customer/', api.CustomerRegistration.as_view(), name='Register-Customer'),

]
