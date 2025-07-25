from django.urls import path
from affairs import views

urlpatterns = [
    # Courier URLs
    path('courier/list', views.CourierListView, name='courier_list'),
    path('courier/create', views.CourierCreateView, name='courier_create'),
    path('courier/update/<int:id>', views.CourierUpdateView, name='courier_update'),
    path('courier/delete/<int:id>', views.CourierDeleteView, name='courier_delete'),

    # Transport URLs
    path('transport/list', views.TransportListView, name='transport_list'),
    path('transport/create', views.TransportCreateView, name='transport_create'),
    path('transport/update/<int:id>', views.TransportUpdateView, name='transport_update'),
    path('transport/delete/<int:id>', views.TransportDeleteView, name='transport_delete'),

    # Delivery URLs
    path('delivery/list', views.DeliveryListView, name='delivery_list'),
    path('delivery/create', views.DeliveryCreateView, name='delivery_create'),
    path('delivery/update/<int:id>', views.DeliveryUpdateView, name='delivery_update'),
    path('delivery/delete/<int:id>', views.DeliveryDeleteView, name='delivery_delete'),

    # Customer URLs
    path('customer/list', views.CustomerListView, name='customer_list'),
    path('customer/create', views.CustomerCreateView, name='customer_create'),
    path('customer/update/<int:id>', views.CustomerUpdateView, name='customer_update'),
    path('customer/delete/<int:id>', views.CustomerDeleteView, name='customer_delete'),

    # Main page
    path('index', views.MainPageView, name='main_page'),
]
