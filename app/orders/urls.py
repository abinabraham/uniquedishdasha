
from django.urls import path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( OrderView, order_ajaxsubmission, order_ajaxcreaion )

app_name = 'orders'

# URLs dashboard
urlpatterns = [
    path('submission/', login_required(OrderView.as_view()), name='order_submission'),
    path('ajax/submission/', login_required(order_ajaxsubmission), name='order_ajax_submission'),    
    path('ajax/orderbook/crud/', login_required(order_ajaxcreaion), name='order_ajaxcreaion'),    

    
]