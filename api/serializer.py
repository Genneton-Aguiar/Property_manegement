from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username','cpf', 'cnpj', 'email', 'telephone', 
            'is_tenant', 'is_owner', 'is_admin', 'is_manager', 'is_operator')

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields =  ('id','user_id', 'name', 'address', 'property_type', 
                   'room_number', 'parking_space', 'avaliable',
                   'rented', 'maintenance')

class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = ('id', 'tenant_id', 'property_id', 'validity', 'start_date', 
                  'end_date', 'rental_value', 'adjustments', 'is_active', 
                  'compliant', 'defaulter')
        
class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('id', 'contract_id', 'payed', 'payment_type',
                  'value_payed', 'date')

class RepasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repasse
        fields = ('user_id', 'payment_id', 'imobiliaria_value',
                  'proprietario_value')
        

        
