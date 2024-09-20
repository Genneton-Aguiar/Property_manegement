from .models import *
from .serializer import *

    
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
