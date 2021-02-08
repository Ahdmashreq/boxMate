from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.db import models
from codes.models import CountryCode, TaxTypes


# Create your models here.
class Issuer(models.Model):
    type = models.CharField(max_length=8,
                            choices=[('B', 'business'), ('P', 'natural person'), ('F', 'foreigner')], default='B')
    reg_num = models.CharField(max_length=8, verbose_name='reg_number')
    name = models.CharField(max_length=50, verbose_name='issuer name', blank=True, null=True)
    client_id = models.CharField(max_length=50,blank=True, null=True )
    clientSecret1 = models.CharField(max_length=50,blank=True, null=True)
    clientSecret2 = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    last_updated_at = models.DateField(null=True, auto_now=True, auto_now_add=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="Issuer_created_by")
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Receiver(models.Model):
    type = models.CharField(max_length=8,
                            choices=[('B', 'business'), ('P', 'natural person'), ('F', 'foreigner')], default='B')
    reg_num = models.CharField(max_length=8, verbose_name='reg_number')
    name = models.CharField(max_length=50, verbose_name='reciever name', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    last_updated_at = models.DateField(null=True, auto_now=True, auto_now_add=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="Receiver_created_by")
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

 
class Address(models.Model):
    branch_id = models.CharField(max_length=10)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE, null=True, blank=True, related_name='issuer_addresses')
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE, null=True, blank=True,related_name='rec_addresses')
    country = models.ForeignKey(CountryCode, on_delete=models.CASCADE, blank=True, null=True)
    governate = models.CharField(max_length=50, blank=True, null=True)
    regionCity = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=120, blank=True, null=True)
    buildingNumber = models.CharField(max_length=120, blank=True, null=True)
    postalCode = models.CharField(max_length=20, blank=True, null=True)
    floor = models.CharField(max_length=10, blank=True, null=True)
    room = models.CharField(max_length=10, blank=True, null=True)
    landmark = models.CharField(max_length=120, blank=True, null=True)
    additionalInformation = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    last_updated_at = models.DateField(null=True, auto_now=True, auto_now_add=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="address_created_by")
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.branch_id



class IssuerTax(models.Model):
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE, null=True, blank=True, related_name='issuer_tax')
    tax_type = models.ForeignKey(TaxTypes, on_delete=models.CASCADE, null=True, blank=True, related_name='issuer_tax_type')
    start_date = models.DateField(default=timezone.now(), null=True, blank=True)
    end_date = models.DateField(auto_now_add=True, null=True, blank=True)
    is_enabled = models.BooleanField()

    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    last_updated_at = models.DateField(null=True, auto_now=True, auto_now_add=False, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="issuer_tax_created_by")
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="issuer_tax_last_update_by")

    def __str__(self):
        return self.issuer.name + ' ' + self.branch_id