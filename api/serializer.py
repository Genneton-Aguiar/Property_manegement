from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'  

class ContratcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratcs
        fields = '__all__'  

class TenantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenants
        fields = '__all__'
        
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'
        
