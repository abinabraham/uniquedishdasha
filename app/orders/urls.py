
from django.urls import path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( OrderView, order_ajaxsubmission, order_ajaxcreaion,
                measurement_ajaxcreaion, complete_order_creation )

app_name = 'orders'

# URLs dashboard
urlpatterns = [
    path('submission/', login_required(OrderView.as_view()), name='order_submission'),
    path('ajax/submission/', login_required(order_ajaxsubmission), name='order_ajax_submission'),    
    path('ajax/orderbook/crud/', login_required(order_ajaxcreaion), name='order_ajaxcreaion'),    
    path('ajax/measurement/crud/', login_required(measurement_ajaxcreaion), name='measurement_ajaxcreaion'),
    path('ajax/order/creation/', login_required(complete_order_creation), name='complete_order_creation'),
    
]