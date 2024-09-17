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
        
        user = Users.objects.filter(pk = request.user.id).first()
        
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem listar usuarios',
                status = HTTP_400_BAD_REQUEST
            )
        
        users= Users.objects.filter(is_active=True)
        users = filter_users(users, request)
        
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
            
    
    def create (self, request, *args, **kwargs):
        
        user = Users.objects.filter(pk = request.user.id).first()
        
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem criar usuarios',
                status = HTTP_400_BAD_REQUEST
            )
        
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
        
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem LISTAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )

        property = Property.objects.all()

        for params in [
            'avaliable',
            'rented',
            'maintenance'
            ]:
            value = request.GET.get(params)
            if value is not None: 
                if value.lower() == 'true':  
                    property = property.filter(**{params: True})
                    
        property_type = request.GET.get('property_type')
        if property_type:
                property = property.filter(property_type=property_type)
        
        serializer = self.get_serializer(property, many=True)
        headers = self.get_success_headers(serializer.data)
        
        return Response(
            serializer.data, 
            status=HTTP_200_OK,
            headers=headers
            )
        
        
    def create (self, request, *args, **kwargs):
        
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem CRIAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )

        data=request.data 
        if not data:
            return Response(
                'informe os dados do evento', 
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
        
        user = Users.objects.filter(pk = request.user.id).first()
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem EDITAR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )

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
        if not request.user.is_authenticated or not user.is_admin:
            return Response(
                'Desculpe, apenas administradores podem EXCLUIR PROPERTYS',
                status = HTTP_400_BAD_REQUEST
            )
            
        property = self.get_object()
        property.delete()
      
        return Response([], status = HTTP_204_NO_CONTENT)

    
    