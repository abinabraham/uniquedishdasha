from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from app.accounts.models import CustomUser
from django.db.models import Q
from django.contrib import messages
from app.api.serializers import UserSerializer, UserAllSerializer
from .utils import render_to_pdf

import json

from app.orders.models import Orders
from app.orders.views import get_balance_status_amount

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"


def origin_airport_search(request):
    term = request.GET.get('term', None)
    return HttpResponse(get_customer_list(term), 'application/json')

def get_customer_list(term):
    customers = []
    if term:
        customers = CustomUser.objects.filter(
            Q(first_name__startswith=term) | Q(last_name__startswith=term)
            | Q(username__startswith=term) | Q(phone_number__contains=term)
            | Q(email__contains=term)).filter(role_name=2)
    data = UserAllSerializer(customers, context={'request': None}, 
                many=True,).data
    result = []
    print(enumerate(data))
    for i, val in enumerate(data):
        first_name = val['first_name'] if val['first_name'] else "-"
        last_name = val['last_name'] if val['last_name'] else "-"
        phone = val['phone_number'] if val['phone_number'] else "-"
        email = val['email'] if val['email'] else "-"
        d = dict()
        d['email'] = email
        d['phone'] = phone
        d['first_name'] = first_name
        d['last_name'] = last_name
        d['id'] = str(val['id'][-4:]) if len(val['id']) > 3 else val['id']
        d['user_id'] = str(val['user_id'])

        d['label']= first_name+" "+last_name
        d['value']= first_name + " " + last_name +" -  (" +email+") - "+ phone 


        result.append(d)
        # result.append('<div class="resultData idData"><span>' +str(val['id'])+ '<div class="resultData nameData"><span>'+first_name+' '+last_name+'</span></div> <div class="resultData emailData"><span>'+email+'</span></div><div class="resultData phoneData"><span>'+phone+'</span></div> ')
    return json.dumps(result)


def update_balance(total, paid_amnt):
    '''
        NOTPAID = 'PS1', 'NOT PAID' 
        PARTPAID = 'PS2', 'PARTIALLY PAID'
        PAID = 'PS3', 'FULLY PAID'
        OVERPAID = 'PS4', 'FULLY PAID'

    '''
    balance = float(total)-float(paid_amnt)
    status = 'PS1'
    if balance == 0:
        status = 'PS3'
    if balance > 0:
        status = 'PS2'
    if balance < 0:
        status = "PS4"
    return balance, status

class DummyView(TemplateView):
    template_name = "dummy.html"

class ProfileView(FormView):
    template_name = "dashboard/profile.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = {'redir':""}
        return redirect("/")
    
    def post(self, request, *args, **kwargs):
        context = {}
        customer_obj = CustomUser.objects.get(
                    user_id=request.POST.get('user_input')
                )
        existing_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS1'
        )
        completed_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS2'
        )
        delivered_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS3'
        )
        context['existing_orders'] = existing_orders
        context['completed_orders'] = completed_orders
        context['delivered_orders'] = delivered_orders
        context['customer_obj'] = customer_obj
        if request.POST.get("order_id"):
            order_id = request.POST.get("order_id")
            complete_order_obj = Orders.objects.get(
                pk = order_id                        
            )
            if request.POST.get('balance_pay'):
                complete_order_obj.total_paid_amount =float(complete_order_obj.total_paid_amount)+float(request.POST.get('balance_pay'))
                complete_order_obj.save()
                balance_amount, status = update_balance(complete_order_obj.total_amnt_to_pay,
                                                complete_order_obj.total_paid_amount)
                complete_order_obj.balance_amount = balance_amount
                complete_order_obj.payment_status = status
                complete_order_obj.save()
            complete_order_obj.order_status = request.POST.get('order_status')
            complete_order_obj.save()
            return redirect("/profile/"+customer_obj.user_id)
        return render(request, self.template_name, context)


class ProfileViewGet(FormView):
    template_name = "dashboard/profile.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = {}
        customer_obj = CustomUser.objects.get(
                    user_id=kwargs.get('id')
                )
        existing_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS1'
        )
        completed_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS2'
        )
        delivered_orders = Orders.objects.filter(
                        customer = customer_obj,
                        order_status = 'OS3'
        )
        context['existing_orders'] = existing_orders
        context['completed_orders'] = completed_orders
        context['delivered_orders'] = delivered_orders
        context['customer_obj'] = customer_obj
        return render(request, self.template_name, context)
    

class PendingOrdersView(FormView):
    template_name = "dashboard/orders_pending.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = {}
        existing_orders = Orders.objects.filter(
                        order_status = 'OS1'
        )
        context['existing_orders'] = existing_orders
        return render(request, self.template_name, context)
from app.orders.models import Orders
from django.shortcuts import get_object_or_404

# pdf
def generatePdf(request,cid,value):
    print(cid,value)
    pdf = render_to_pdf('orders/pdf/invoice.html',cid)
    return HttpResponse(pdf, content_type='application/pdf')

def generatePrint(request,cid):
    print(cid)
    node = get_object_or_404(Orders, id =cid)
    context = {'node':node}
    return render(request, 'orders/pdf/invoice.html', context)