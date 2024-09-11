from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_409_CONFLICT,
)

from .models import *
from .serializer import *


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer
    
    def list (self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)
    
    def create (self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    def list (self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def cretate (self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class ContratcsViewSet(viewsets.ModelViewSet):
    queryset = Contratcs.objects.all()
    serializer_class = ContratcsSerializer

    def list (self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)
    
    def create (self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
class TenantsViewSet(viewsets.ModelViewSet):
    queryset = Tenants.objects.all()
    serializer_class = TenantsSerializer
    
    def list (self, request, *args, **kwargs):  
        return super().list(request, *args, **kwargs)
    
    def create (self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    
    def list (self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create (self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

