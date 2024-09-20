from .models import *
from .serializer import *

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)



def create_users(data):
    
    cpf = data.get('cpf')
    cnpj = data.get('cnpj')
    name = data.get('username')
    email = data.get('email')
    telephone = data.get('telephone')
    is_tenant = data.get('is_tenant')
    is_owner = data.get('is_owner')
    password = data.get('password')
    admin = data.get('is_admin')
    manager = data.get('is_manager')
    operator = data.get('is_operator')

    user = Users.objects.create(
        cpf = cpf,
        cnpj = cnpj,
        username = name,
        email = email,
        telephone = telephone,
        is_tenant = is_tenant,
        is_owner = is_owner,
        is_admin = admin,
        is_manager = manager,
        is_operator = operator,
        password = password,
    )
    return user


def filter_users(users, request):
    
    for params in [
        'is_tenant', 
        'is_owner', 
        'is_admin', 
        'is_manager', 
        'is_operator'
    ]:
        value = request.GET.get(params)
        if value is not None: 
            if value.lower() == 'true':  
                users = users.filter(**{params: True})
    
    name = request.GET.get('username')
    if name:
        users = users.filter(username__icontains=name)

    cpf = request.GET.get('cpf')
    if cpf:
        users = users.filter(cpf=cpf)
 
    return users


def create_property(data):
    
# valor de 'user_id' do dicionário de dados

    user_id = data.get('user_id')  
    user = Users.objects.get(id=user_id)

    name = data.get('name')
    address = data.get('address')
    property_type = data.get('property_type')
    room_number = data.get('room_number')
    parking_space = data.get('parking_space')
    rental_value = data.get('rental_value')
    avaliable = data.get('avaliable')
    rented = data.get('rented')
    maintenance = data.get('maintenance')
   
    property = Property.objects.create(
        user_id = user.id,
        name = name,
        address = address,
        property_type = property_type,
        room_number = room_number,
        parking_space = parking_space,
        rental_value = rental_value,
        avaliable = avaliable,
        rented = rented,
        maintenance = maintenance
    )
    return property


def filter_contracts(contracts, request):
    
    
    params = ['user_id', 'property_id']
    for param in params:
        value = request.GET.get(param)
        if value is not None: 
            if value.isdigit():  
                contracts = contracts.filter(**{param: int(value)})
    
    compliant = request.GET.get('compliant')
    if compliant is not None:
        if compliant.lower() == 'true':
            contracts = contracts.filter(compliant=True)
        elif compliant.lower() == 'false':
            contracts = contracts.filter(compliant=False)
    
    is_active = request.GET.get('is_active')
    if is_active is not None:
        if is_active.lower() == 'true':
            contracts = contracts.filter(is_active=True)
        elif is_active.lower() == 'false':
            contracts = contracts.filter(is_active=False)

    return contracts


def create_contract(data):

    user_id = data.get('user_id')  
    user = Users.objects.get(id=user_id)
    
    if not user.is_tenant:
        return Response(
            'Desculpe, apenas inquilinos podem criar contratos',
            status = HTTP_400_BAD_REQUEST
        )

    property_id = data.get('property_id')
    property = Property.objects.get(id=property_id)
    
    if not property.avaliable:
        return Response(
            'Desculpe, esta propriedade ja foi alugada',
            status = HTTP_400_BAD_REQUEST
        )
        
    validity = data.get('validity')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    rental_value = data.get('rental_value')
    adjustments = data.get('ajustments')
    compliant= data.get('compliant')
    defaulter = data.get('defaulter')
    
    

    contract = Contracts.objects.create(
        user_id= user.id,
        property_id = property.id,
        validity = validity,
        start_date = start_date,
        end_date = end_date,
        rental_value = rental_value,
        adjustments= adjustments,
        is_active= True,
        compliant = compliant,
        defaulter = defaulter
    )
    
    return contract


def  create_payment(data, request):
    
    contract_id = data.get('contracts_id')
    contract = Contracts.objects.get(id=contract_id)
    
    payed= data.get('payed')
    payment_type = data.get('payment_type')
    value_payed = data.get('value_payed')
    date = data.get('date')
    
    
    payment = Payments.objects.create(
        user_id = request.user.id,
        contract_id = contract.id,
        payed = payed,
        payment_type = payment_type,
        value_payed = value_payed,
        date = date
    )

    if not payed:
        contract.defaulter = True
        contract.save()
        
    return payment



