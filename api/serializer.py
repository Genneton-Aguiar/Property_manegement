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

        
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

class RepasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repasse
        fields = '__all__'
        

        
