from django.contrib import admin
from .models import TransportModel,CustomerModel,CourierModel,DeliveryModel

# Register your models here.
admin.site.register(TransportModel)
admin.site.register(CustomerModel)
admin.site.register(DeliveryModel)
admin.site.register(CourierModel)