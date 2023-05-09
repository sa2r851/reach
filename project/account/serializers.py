from rest_framework import serializers
from .models import *

class PharmacySerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(default="PHARMACY")
    class Meta:
        model = Pharmacy
        fields=['username','city','country','password','address','phone_number','role']
    def create(self, validated_data):
        user = Pharmacy(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomerSerializer(serializers.ModelSerializer):
    role = serializers.ReadOnlyField(default="CUSTOMER")
    class Meta:
        model = Customer
        fields=['username','city','country','password',"address",'phone_number','role']
    def create(self, validated_data):
        user = Customer(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user