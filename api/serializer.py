from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username','cpf', 'cnpj', 'email', 'telephone', 
            'is_tenant', 'is_owner', 'is_admin', 'is_manager', 'is_operator',
            'password')

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields =  ('id','user_id', 'name', 'address', 'property_type', 
                   'room_number', 'parking_space', 'rental_value', 'avaliable',
                   'rented', 'maintenance')

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
        

        
