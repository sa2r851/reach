from django.urls import path
from . import api
app_name='account'
urlpatterns = [
    #create account
    path('register-ph/', api.PharmacyRegistration.as_view(), name='Register-Pharmacy'),
    path('register_customer/', api.CustomerRegistration.as_view(), name='Register-Customer'),
    path("branch_cities",api.branch_cities,name='cities of branch'),
    path("branch_staff",api.branch_staff,name='staff branch'),
    path("city_customer",api.city_customer,name='Customers of city'),

]
