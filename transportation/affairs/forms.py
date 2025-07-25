from .models import CourierModel, CustomerModel, TransportModel,DeliveryModel
from django import forms

class CourierForm(forms.ModelForm):
    class Meta:
        model = CourierModel
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = '__all__'

class TransportForm(forms.ModelForm):
    class Meta:
        model = TransportModel
        fields = '__all__'


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryModel
        fields = '__all__'