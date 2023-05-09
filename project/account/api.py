from .models import *
from .serializers import *
from rest_framework import generics

class PharmacyRegistration(generics.CreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class CustomerRegistration(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer