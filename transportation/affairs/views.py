from django.shortcuts import render
from .models import CourierModel, TransportModel, DeliveryModel, CustomerModel
from .forms import TransportForm, DeliveryForm, CustomerForm, CourierForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from affairs import views
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def CourierListView(request):
    couriers = CourierModel.objects.all()

    context = {
        'courier': couriers
    }

    return render(request,'affairs/CourierList.html',context)

@login_required
def CourierCreateView(request):
    if request.method == 'POST':
        courierForm = CourierForm(request.POST)
        if courierForm.is_valid:
            courierForm.save()
            return HttpResponseRedirect(reverse(views.CourierListView))
    else:
        courierForm = CourierForm()

    context = {
        'coForm': courierForm
    }

    return render(request,'affairs/CourierCreate.html',context)

@login_required
def CourierUpdateView(request,id):
    cInstance = CourierModel.objects.get(pk=id)
    if request.method == 'POST':
        courierForm = CourierForm(request.POST,instance=cInstance)
        if courierForm.is_valid:
            courierForm.save()
            return HttpResponseRedirect(reverse(views.CourierListView))
    else:
        courierForm = CourierForm(instance=cInstance)

    context = {
        'coForm': courierForm
    }

    return render(request,'affairs/CourierUpdate.html',context)

@login_required
def CourierDeleteView(request,id):
    cInstance = CourierModel.objects.get(pk=id)
    cInstance.delete()
    return HttpResponseRedirect(reverse(views.CourierListView))
    

def TransportListView(request):
    transports = TransportModel.objects.all()

    context = {
        'transports': transports
    }
    return render(request,'affairs/TransportList.html',context)

@login_required
def TransportCreateView(request):
    if request.method == 'POST':
        transportForm = TransportForm(request.POST)
        if transportForm.is_valid:
            transportForm.save()
            return HttpResponseRedirect(reverse(views.TransportListView))
    else:
        transportForm = TransportForm()

    context = {
        'tForm': transportForm
    }

    return render(request,'affairs/TransportCreate.html',context)

@login_required
def TransportUpdateView(request,id):
    tInstance = TransportModel.objects.get(pk=id)
    if request.method == 'POST':
        transportForm = TransportForm(request.POST,instance=tInstance)
        if transportForm.is_valid:
            transportForm.save()
            return HttpResponseRedirect(reverse(views.TransportListView))
    else:
        transportForm = TransportForm(instance=tInstance)

    context = {
        'tForm': transportForm
    }

    return render(request,'affairs/TransportUpdate.html',context)

@login_required
def TransportDeleteView(request,id):
    tInstance = TransportModel.objects.get(pk=id)
    tInstance.delete()
    return HttpResponseRedirect(reverse(views.TransportListView))



def DeliveryListView(request):
    deliveries = DeliveryModel.objects.all()

    context = {
        'deliveries': deliveries
    }
    return render(request,'affairs/DeliveryList.html',context)

@login_required
def DeliveryCreateView(request):
    if request.method == 'POST':
        deliveryForm = DeliveryForm(request.POST)
        if deliveryForm.is_valid:
            deliveryForm.save()
            return HttpResponseRedirect(reverse(views.DeliveryListView))
    else:
        deliveryForm = DeliveryForm()

    context = {
        'dForm': deliveryForm
    }

    return render(request,'affairs/DeliveryCreate.html',context)


@login_required
def DeliveryUpdateView(request,id):
    dInstance = DeliveryModel.objects.get(pk=id)
    if request.method == 'POST':
        deliveryForm = DeliveryForm(request.POST,instance=dInstance)
        if deliveryForm.is_valid:
            deliveryForm.save()
            return HttpResponseRedirect(reverse(views.DeliveryListView))
    else:
        deliveryForm = DeliveryForm(instance=dInstance)

    context = {
        'dForm': deliveryForm
    }

    return render(request,'affairs/DeliveryUpdate.html',context)

@login_required
def DeliveryDeleteView(request,id):
    dInstance = DeliveryModel.objects.get(pk=id)
    dInstance.delete()
    return HttpResponseRedirect(reverse(views.DeliveryListView))

@login_required
def CustomerListView(request):
    customers = CustomerModel.objects.all()

    context = {
        'customers': customers
    }
    return render(request,'affairs/CustomerList.html',context)


def CustomerCreateView(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid:
            customerForm.save()
            return HttpResponseRedirect(reverse(views.CustomerListView))
    else:
        customerForm = CustomerForm()

    context = {
        'cForm': customerForm
    }

    return render(request,'affairs/CustomerCreate.html',context)

@login_required
def CustomerUpdateView(request,id):
    cInstance = CustomerModel.objects.get(pk=id)
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST,instance=cInstance)
        if customerForm.is_valid:
            customerForm.save()
            return HttpResponseRedirect(reverse(views.CustomerListView))
    else:
        customerForm = CustomerForm(instance=cInstance)

    context = {
        'cForm': customerForm
    }

    return render(request,'affairs/CustomerUpdate.html',context)

@login_required
def CustomerDeleteView(request,id): 
    try:   
        cInstance = CustomerModel.objects.get(pk=id)
        cInstance.delete()
        return HttpResponseRedirect(reverse(views.CustomerListView))
    except:
        return HttpResponse('Integrity Problem')
        


def MainPageView(request):
    return render(request,'affairs/index.html',{})