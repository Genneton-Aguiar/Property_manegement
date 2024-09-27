from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from .utils import *

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)

from .models import *
from .serializer import *


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
    def list (self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem listar usuarios',
                status = HTTP_400_BAD_REQUEST
            )'''
        
        users = Users.objects.filter(is_active=True)
        
        users = filter_users(users, request)
 
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
            

    def create (self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem criar usuarios',
                status = HTTP_400_BAD_REQUEST
            )'''
        
        data = request.data
        if not data:
            return Response(
                'informe os dados do usuario', 
                status=HTTP_400_BAD_REQUEST
                )

        user = create_users(data)
        
        serializer = self.get_serializer(user)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data, 
            status = HTTP_201_CREATED, 
            headers=headers
            )
        
        
    def partial_update(self, request, pk):
        
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem editar usuarios',
                status = HTTP_400_BAD_REQUEST
            )
        try:
                users = Users.objects.get(pk=pk)
                data = request.data
                
                serializer = UsersSerializer(users, data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=HTTP_200_OK)
                    
        except Exception as e:
                return Response(e, status=HTTP_400_BAD_REQUEST)   
   

    def destroy(self, request, **kwargs):   
        
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem deletar usuarios',
                status = HTTP_400_BAD_REQUEST
            )
            
        users = self.get_object()
        users.delete()
      
        return Response([], status = HTTP_204_NO_CONTENT)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list (self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or (not user.is_admin 
            and not user.is_manager and not user.is_operator):
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem LISTAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )'''

        property = Property.objects.all()

        property = filter_property(property, request)
        
        serializer = self.get_serializer(property, many=True)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data, 
            status=HTTP_200_OK,
            headers=headers
            )
        
        
    def create (self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or (not user.is_admin 
            and not user.is_manager):
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem CRIAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )'''

        data=request.data 
        if not data:
            return Response(
                'informe os dados da propriedade', 
                status=HTTP_400_BAD_REQUEST
                )
            
        property = create_property(data)
        
        serializer = self.get_serializer(property)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
            )
        
    def partial_update(self, request, pk):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or (not user.is_admin 
            and not user.is_manager):
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem EDITAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )'''

        try:
            property = Property.objects.get(pk=pk)
            data = request.data
            
            serializer = PropertySerializer(property, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_200_OK)
                
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, **kwargs):  
         
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or (not user.is_admin 
            and not user.is_manager):
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem DELETAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )
            
        property = self.get_object()
        property.delete()
      
        return Response([], status = HTTP_204_NO_CONTENT)


class ContractsViewSet(viewsets.ModelViewSet):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

    def list (self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem LISTAR CONTRATCS',
                status = HTTP_400_BAD_REQUEST
            )'''
        
        contracts= Contracts.objects.all()
        
        contracts= filter_contracts(contracts, request)
                        
        serializer = ContractsSerializer(contracts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
            
    def create(self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Apenas ADMINISTRADORES e GESTORES podem CRIAR CONTRATCS',
                status = HTTP_400_BAD_REQUEST
            )'''

        data=request.data 
        if not data:
            return Response(
                'informe os dados do contrato', 
                status=HTTP_400_BAD_REQUEST
                )
            
        contract = create_contract(data)

        serializer = self.get_serializer(contract)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
            )

    def partial_update(self, request, pk):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Apenas ADNIMINADORES e GESTORES podem EDITAR CONTRATCS',
                status = HTTP_400_BAD_REQUEST
            )'''

        try:
            property = Property.objects.get(pk=pk)
            data = request.data
            
            serializer = PropertySerializer(property, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=HTTP_200_OK)
                
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem deletar usuarios',
                status = HTTP_400_BAD_REQUEST
            )'''
            
        contract = self.get_object()
        contract.is_active=False
        contract.save()
        
        
        return Response([], status = HTTP_204_NO_CONTENT)
    
    
class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def list (self, request, *args, **kwargs):    

        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem LISTAR  PAYMENTS',  
                status = HTTP_400_BAD_REQUEST
            )'''

        payments= Payments.objects.all()
            
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):


        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem CRIAR PAYMENTS',
                status = HTTP_400_BAD_REQUEST
            )'''
        
        data=request.data 
        if not data:
            return Response(
                'informe os dados do pagamento', 
                status=HTTP_400_BAD_REQUEST
                )
            
        payment = create_payment(data,request)

        serializer = self.get_serializer(payment)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data,
            status=HTTP_201_CREATED,
            headers=headers
            )

    
    def paginate_queryset(self, queryset):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem LISTAR PAYMENTS',
                status = HTTP_400_BAD_REQUEST
            )'''

        return super().paginate_queryset(queryset)
    
    
    def destroy(self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem EXCLUIR PAYMENTS',
                status = HTTP_400_BAD_REQUEST
            )'''

        return super().destroy(request, *args, **kwargs)


class RepasseViewSet(viewsets.ModelViewSet):
    queryset = Repasse.objects.all()
    serializer_class = RepasseSerializer

    def list(self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem EXCLUIR PAYMENTS',
                status = HTTP_400_BAD_REQUEST
            )'''
        
        Repasse = Repasse.objects.all()

        serializer = RepasseSerializer(Repasse, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        
        '''user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem EXCLUIR PAYMENTS',
                status = HTTP_400_BAD_REQUEST
            )'''
            
        data = request.data

        owner_id =  data.get('owner_id')
        user = Users.objects.get(id=owner_id)
        
        payment_id= data.get('payment_id')
        payment = Payments.objects.get(id=payment_id)
        
        repasse = Repasse.objects.create(
            user_id= user.id,
            Payments_id=payment.id,
        )

        value = payment.value
        imobiliaria = value * 0.30
        proprietario = value * 0.70

        repasse.imobiliaria_value = imobiliaria
        repasse.proprietario_value = proprietario

        
        serializer = self.get_serializer(repasse)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
