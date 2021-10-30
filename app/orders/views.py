from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app.accounts.models import CustomUser, Branch
from django.http import JsonResponse, HttpResponseBadRequest
from app.api.serializers import UserSerializer, UserAllSerializer, \
                              CompleteOrdersSerializer, OrderBookSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import (Measurements, OrderBook, FabricType,
                     TailoringStyle, Orders, PricingPlans )

class OrderView(FormView):
    template_name = "orders/orders_1.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = {'redir':""}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        print("--------------->",request.POST.get('user_input', None))
        try:
            user_id = request.POST.get('user_input', None).split(", ")[1]
            user_id_frmttd = user_id.replace('(', '').replace(')', '')
            customer = CustomUser.objects.get(
                    pk = int(user_id_frmttd)
            )
        except:
            customer =  None
        context = {'customer':customer}
        return render(request, self.template_name, context)

@csrf_exempt
def order_ajaxsubmission(request):
    # request should be ajax and method should be POST.
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:        
        fields = ['first_name','last_name','email','address','place', \
                'area','phone_number','notes']
        data = {k:v for (k,v) in request.POST.items() if k in fields}
        data['username'] = request.POST.get('email')
        try:
            branch_obj, created = Branch.objects.get_or_create(
                            title='Salhia'
                        )
            obj, created = CustomUser.objects.update_or_create(
                username=data['username'],
                defaults=data,
            )
            obj.role_name = 2
            obj.is_verified = True
            obj.is_profile_completed = True
            obj.branch = branch_obj

            obj.save()
            customer_obj = UserAllSerializer(obj, context={'request': None}).data
            return JsonResponse({"success": "Succesfully Saved customer", 'data':customer_obj}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

def get_price_per_unit(tailr_styl_obj):
    amount = PricingPlans.objects.filter(
                 tailr_styl = tailr_styl_obj,
                  is_active=True)[0].amount
    return amount

def get_balance_status_amount(total, paid_amnt):
    '''
        NOTPAID = 'PS1', 'NOT PAID' 
        PARTPAID = 'PS2', 'PARTIALLY PAID'
        PAID = 'PS3', 'FULLY PAID'
        OVERPAID = 'PS4', 'FULLY PAID'

    '''
    balance = float(total) - float(paid_amnt)
    if balance == 0:
        status = 'PS3'
    if balance > 0:
        status = 'PS2'
    else:
        status = "PS4"
    return balance, status

@csrf_exempt
def order_ajaxcreaion(request):
    # request should be ajax and method should be POST.
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        try:
            data = dict()
            branch_obj, created = Branch.objects.get_or_create(
                                title='Salhia'
                            )
            customer_obj = CustomUser.objects.get(
                                id=request.POST.get('session_customer')
                            )
            fab_obj = FabricType.objects.get(id = request.POST.get('fabricType'))
            taistyle_obj = TailoringStyle.objects.get(id = request.POST.get('tayloringType'))
            qty = int(request.POST.get('qty'))
            order_list = list()
            complete_order_obj = Orders(
                        customer = customer_obj,                        
                    )
            complete_order_obj.save()
            for qt in range(qty):
                data['branch'] = branch_obj
                data['customer'] = customer_obj
                data['is_customer_own_fabric'] = True if request.POST.get('flexRadioDefault')=='on' else False
                data['fb_type'] = fab_obj
                data['tailr_styl'] = taistyle_obj
                data['color'] = request.POST.get('color')
                data['total_meters'] = request.POST.get('meters')
                data['quantity'] = request.POST.get('qty')
                data['deliver_at'] = request.POST.get('ddate')
                obj = OrderBook.objects.create(
                        **data
                    )            
                order_obj = OrderBookSerializer(obj, context={'request': None}).data
                order_list.append(order_obj)

                price_unit = get_price_per_unit(taistyle_obj)
                complete_order_obj.total_amnt_to_pay += price_unit
                complete_order_obj.orders.add(obj)
                complete_order_obj.save()
            customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
            return JsonResponse({"success": "Succesfully order booked", 'data':{'data':order_list,'user':customer_obj,
                                 'branch_title':branch_obj.title, 'qty':qty, 'complete_order_id':complete_order_obj.pk}}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')



        
@csrf_exempt
def measurement_ajaxcreaion(request):
    # request should be ajax and method should be POST.      
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        try:
            data = dict()
            order_obj = OrderBook.objects.get(
                            pk = request.POST.get('session_measure_order')
                        )
            branch_obj, created = Branch.objects.get_or_create(
                                title='Salhia'
                            )
            customer_obj = CustomUser.objects.get(
                                id=request.POST.get('session_measure_user')
                            )
            data = dict()
            data['order'] = order_obj
            data['collar'] = request.POST.get('collar')
            data['zip'] = request.POST.get('zip')
            data['pocket'] = request.POST.get('zip')
            data['pockettwo'] = request.POST.get('pocketTwo')
            data['tie'] = request.POST.get('tie')
            data['penpocket'] = request.POST.get('penpocket') 
            data['sholderOne'] = request.POST.get('sholderOne')    
            data['sholderTwo'] = request.POST.get('sholderTwo')    
            data['mainWidth'] = request.POST.get('mainWidth')   
            data['penPocket_select'] = request.POST.get('penPocket')   
            data['insidePocket'] = request.POST.get('insidePocket')  
            data['handSize'] = request.POST.get('handSize')  
            data['cufflink'] = request.POST.get('cufflink') 
            data['insidepocketshape'] = request.POST.get('insidePocketShape') 
            data['button'] = request.POST.get('buttons') 
            data['finalstyle'] = request.POST.get('finalStyle') 

            data['width_collar'] = request.POST.get('width_collar') 
            data['size_collar'] = request.POST.get('size_collar') 
            data['shoulder'] = request.POST.get('shoulder') 
            data['front_chest'] = request.POST.get('front_chest') 

            data['bar'] = request.POST.get('bar') 
            data['sleeve_length'] = request.POST.get('sleeve_length') 
            data['front_pocket'] = request.POST.get('front_pocket') 
            data['size_pocket'] = request.POST.get('size_pocket') 
            data['big_pocket'] = request.POST.get('big_pocket') 
              
            data['fold_width'] = request.POST.get('fold_width') 
            data['fold_length'] = request.POST.get('fold_length') 
            data['two_line'] = request.POST.get('two_line') 
            data['length'] = request.POST.get('length') 

            
            complete_order_obj = Orders.objects.get(
                        pk = request.POST.get('session_measure_complete_order')                        
                    )            
            obj = Measurements.objects.create(
                                **data
                            )
            complete_order_obj.measurements.add(obj)
            complete_order_obj.save()
            order_obje = OrderBookSerializer(order_obj, context={'request': None}).data
            customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
            fab_title = order_obj.fb_type.title
            tailr_title = order_obj.tailr_styl.title

            comp_ordr_obj = CompleteOrdersSerializer(complete_order_obj,context={'request': None}).data
            return JsonResponse({"success": "Succesfully measure noted", 'data':{'order':order_obje,
                                        'customer':customer_obj,'comp_ordr_obj':comp_ordr_obj,
                                         'fab_title':fab_title,'tailr_title':tailr_title }}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


@csrf_exempt
def complete_order_creation(request):   
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        try:
            complete_order_obj = Orders.objects.get(
                pk = request.POST.get('session_complete_order')                        
            )
            complete_order_obj.payment_status = request.POST.get('pay_methd')
            complete_order_obj.total_paid_amount = request.POST.get('pay_amount')
            balance_amount, status = get_balance_status_amount(complete_order_obj.total_amnt_to_pay,
                                               request.POST.get('pay_amount'))
            complete_order_obj.balance_amount = balance_amount
            complete_order_obj.payment_status = status

            complete_order_obj.save()
            return JsonResponse({"success": "Succesfully created order", 'data':{}}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
