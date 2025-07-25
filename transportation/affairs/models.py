from django.db import models

# Create your models here.

class TransportModel(models.Model):    
    departDate = models.DateField()
    arrivalDate = models.DateField()
    vehicleNo = models.CharField(max_length=100)
    courierId = models.ForeignKey("CourierModel",on_delete=models.PROTECT)
    source = models.CharField(max_length=100, null=True)
    destination = models.CharField(max_length=100, null= True)
    customerId = models.ForeignKey('CustomerModel',on_delete=models.PROTECT)

class CustomerModel (models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    identityNo = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return 'Customer fullname is: {}{}'.format(self.name,self.surname)

class DeliveryModel(models.Model):
    dateTime = models.DateTimeField()
    isSuccessfull = models.BooleanField(default= False)
    courierId = models.ForeignKey("CourierModel",on_delete=models.PROTECT)

class CourierModel(models.Model):
    courierId = models.IntegerField(primary_key=True)
    cName = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.cName