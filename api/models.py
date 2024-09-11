from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Users(User):
    cpf= models.CharField(
        verbose_name="CPF", 
        max_length=11, 
        unique=True
    )
    cnpj= models.CharField(
        verbose_name="CNPJ", 
        max_length=14, 
        unique=True
    )
    telephone= models.CharField(
        verbose_name="Telefone", 
        max_length=11
    )
    is_owner= models.BooleanField(
        verbose_name="é proprietario?", 
        default=False
    )
    is_tenant= models.BooleanField(
        verbose_name="é inquilino?", 
        default=False
    )
    is_admin= models.BooleanField(
        verbose_name="Admin", 
        default=False
    )
    is_manager= models.BooleanField(
        verbose_name="Gestor", 
        default=False
    )
    is_operator= models.BooleanField(
        verbose_name="Operador", 
        default=False
    )
    
    def __str__(self):
        return self.username


class Property(models.Model):
    
    AP='APARTAMENTO'
    HOUSE='CASA'
    COMERCIAL='COMERCIAL'
    
    TYPE_CHOICES = [
        (AP, 'Apartamento'),
        (HOUSE, 'Casa'),
        (COMERCIAL, 'Comercial'),
    ]
    
    property_type= models.CharField(
        verbose_name="Tipo", 
        max_length=100,
        choices=TYPE_CHOICES
    )
    user = models.ForeignKey(
        Users, 
        verbose_name="Usuario",
        on_delete=models.DO_NOTHING
        )
    
    name= models.CharField(
        verbose_name="Nome", 
        max_length=100
    )
    address= models.CharField(
        verbose_name="Endereço", 
        max_length=150
    )
    room_number= models.IntegerField(
        verbose_name="Numero de quartos", 
        default=1
    )
   
    parking_space= models.IntegerField(
        verbose_name="Vagas de estacionamento", 
        default=1
    )
    rental_value= models.FloatField(
        verbose_name="Valor de aluguel", 
        default=0
    )
    available= models.BooleanField(
        verbose_name="Disponível", 
        default=True
    )
    rented= models.BooleanField(
        verbose_name="Alugado", 
        default=False
    )
    maintenance= models.BooleanField(
        verbose_name="Em manutenção", 
        default=False
    )
    
    def __str__(self):
        return self.name
    

class Contratcs(models.Model):
    BOLETO='BOLETO'
    TRANSF_BANC='TRANSFERENCIA_BANCARIA'
    
    TYPE_CHOICES = [
        (BOLETO, 'Boleto'),
        (TRANSF_BANC, 'Transferência bancária'),
    ]
    
    payment_type= models.CharField(
        verbose_name="Tipo de pagamento", 
        max_length=100,
        choices=TYPE_CHOICES
    )
    
    user = models.ForeignKey(
        Users, 
        verbose_name="Usuario",
        on_delete=models.DO_NOTHING
        )
    property = models.ForeignKey(
        Property, 
        verbose_name="Imovel",
        on_delete=models.DO_NOTHING
    )
    validity = models.DateField(
        verbose_name="Validade", 
        default=timezone.now
    )
    start_date = models.DateField(
        verbose_name="Data de inicio", 
        default=timezone.now
    )
    end_date = models.DateField(
        verbose_name="Data de fim", 
        default=timezone.now
    ) 
    adjustments= models.FloatField(
        verbose_name="Ajustes previstos", 
        default=0
    )
    is_active= models.BooleanField(
        verbose_name="contrato encerrado", 
        default=False
    )
    devolution_reason = models.CharField(
        verbose_name="Motivo da devolução", 
        max_length=100
    )
    compliant= models.BooleanField(
        verbose_name="adimplente",
        default=False
    )
    defaulter = models.BooleanField(
        verbose_name="inadimplente",
        default=False
    )
    
    
    def __str__(self):
        return self.user
    
    
class Tenants(models.Model):
    
    user = models.ForeignKey(
        Users, 
        verbose_name="inquilino",
        on_delete=models.DO_NOTHING
        )
    
    contract= models.ForeignKey(
        Contratcs, 
        verbose_name="Contrato",
        on_delete=models.DO_NOTHING
        )
    
    property = models.ForeignKey(
        Property, 
        verbose_name="Imovel",
        on_delete=models.DO_NOTHING
    )
    
    def __str__(self):
        return self.user
    
    
class Payments(models.Model):
    
    contratc= models.ForeignKey(
        Contratcs, 
        verbose_name="tipo de pagamento",
        on_delete=models.DO_NOTHING
        )
    
    value_payed = models.FloatField(
        verbose_name="Valor pago", 
        default=0
    )
    
    date= models.DateField(
        verbose_name="Data do pagamento", 
        default=timezone.now
    )

    def __str__(self):
        return self.contratc
    
    
class Owner (models.Model):

    user = models.ForeignKey(
        Users,
        verbose_name="proprietario",
        on_delete=models.DO_NOTHING
    )
    
    payment= models.ForeignKey(
        Payments,
        verbose_name="pagamento",
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.user
    

