
from django.urls import path
from django.contrib.auth.decorators import login_required

#Custom Imports
from .views import ( OrderView, order_ajaxsubmission )

app_name = 'orders'

# URLs dashboard
urlpatterns = [
    path('submission/', login_required(OrderView.as_view()), name='order_submission'),
    path('ajax/submission/', login_required(order_ajaxsubmission), name='order_ajax_submission'),    
]