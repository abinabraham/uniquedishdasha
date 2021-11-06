from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app.accounts.models import CustomUser, Branch
from django.http import JsonResponse, HttpResponseBadRequest
from app.api.serializers import UserSerializer, UserAllSerializer, \
                              CompleteOrdersSerializer, MeasurementsSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum

from .models import (Measurements,  FabricType,
                     TailoringStyle, Orders, PricingPlans,
                     PricingPlansFabricTyp )
from app.dashboard.models import Colors


class OrderView(FormView):
    template_name = "orders/orders_1.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        try:
            user_id = user_id=kwargs.get('uid', None)
            customer = CustomUser.objects.get(
                    pk = user_id
            )
        except Exception as e:
            print(e)
            customer =  None
        context = {'customer':customer}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.POST.get('user_input', None)
            customer = CustomUser.objects.get(
                    pk = int(user_id)
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

def get_price_per_unit(tailr_styl_obj,fab_obj,fab_status):
    amount,fab_amount = 0,0
    try:
        amount = PricingPlans.objects.filter(
                        tailr_styl = tailr_styl_obj,
                        is_active=True)[0].amount
    except:
        amount = 0
    if not fab_status:
        try:
            fab_amount = PricingPlansFabricTyp.objects.filter(
                    fabr_typ = fab_obj,
                    is_active=True)[0].amount
        except:
            fab_amount = 0
    print("statussssssss",fab_status)
    print("amount",fab_amount, amount)

    return amount+fab_amount

def get_balance_status_amount(total, paid_amnt):
    '''
        NOTPAID = 'PS1', 'NOT PAID' 
        PARTPAID = 'PS2', 'PARTIALLY PAID'
        PAID = 'PS3', 'FULLY PAID'
        OVERPAID = 'PS4', 'OVER PAID'

    '''
    balance = int(float(total)-float(paid_amnt))
    status = 'PS1'
    if balance == 0:
        status = 'PS3'
    if balance > 0:
        status = 'PS2'
    if balance < 0:
        status = "PS4"
    return balance, status

@csrf_exempt
def order_ajaxcreaion(request):
    # request should be ajax and method should be POST.
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        try:
            data = dict()
            branches_selection =  request.POST.get('branch', None)
            try:
                branch_obj,created  = Branch.objects.get_or_create(
                        pk = int(branches_selection)
                )
            except:
                branch_obj = Branch.objects.all()[0]
            customer_obj = CustomUser.objects.get(
                                user_id=request.POST.get('session_customer')
                            )
            
            qty = int(request.POST.get('qty'))
            order_list = list()
            data['branch'] = branch_obj
            data['customer'] = customer_obj
            data['is_customer_own_fabric'] = True if request.POST.get('flexRadioDefault')=='Yes' else False
            data['quantity'] = request.POST.get('qty')
            data['deliver_at'] = request.POST.get('ddate')
            complete_order_obj = Orders(
                        **data                        
                    )
            complete_order_obj.save()
            try:
                latest_measure = Orders.objects.filter(
                    customer = customer_obj
                ).order_by('created_at')[0].measurements.all()
                if latest_measure:
                    latest_measure = latest_measure[0]
                else:
                    latest_measure = None
            except Exception as e:
                print("============e",e)
                latest_measure = None
            latest_measure_obj = MeasurementsSerializer(latest_measure).data
            comp_ordr_obj = CompleteOrdersSerializer(complete_order_obj,context={'request': None}).data

            customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
           
            return JsonResponse({"success": "Succesfully order booked", 'data':{'data':comp_ordr_obj,'user':customer_obj,
                                 'branch_title':branch_obj.title, 'qty':qty, 'complete_order_id':complete_order_obj.pk,
                                 "latest_measure":latest_measure_obj}}, status=200)
        except Exception as error:
            print("erorrrrrrrrrrrrr",error)
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
            branch_obj, created = Branch.objects.get_or_create(
                                title='Salhia'
                            )
            customer_obj = CustomUser.objects.get(
                                user_id=request.POST.get('session_measure_user')
                            )
            fab_obj = FabricType.objects.get(id = request.POST.get('fabricTypes'))
            taistyle_obj = TailoringStyle.objects.get(id = request.POST.get('tayloringType'))
            data = dict()
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
            try:
                color = Colors.objects.get(id=request.POST.get('color'))
            except:
                color = None
            data['color'] = color.name if color else request.POST.get('color')
            data['total_meters'] = request.POST.get('meters')
            data['fb_type'] = fab_obj
            data['tailr_styl'] = taistyle_obj


            
            complete_order_obj = Orders.objects.get(
                        pk = request.POST.get('session_measure_complete_order')                        
                    )            
            obj = Measurements.objects.create(
                                **data
                            )

            is_customer_own_fabric = complete_order_obj.is_customer_own_fabric
            price_unit = get_price_per_unit(taistyle_obj,fab_obj,is_customer_own_fabric)
            obj.price = price_unit
            obj.save()                 

            complete_order_obj.measurements.add(obj)
            complete_order_obj.save()
            try:
                total_price = complete_order_obj.measurements.aggregate(TOTAL = Sum('price'))['TOTAL']
            except:
                total_price = 0
            complete_order_obj.total_amnt_to_pay = float(total_price) if total_price else 0
            complete_order_obj.save()

            order_obje = CompleteOrdersSerializer(complete_order_obj, context={'request': None}).data
            customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
            fab_title = fab_obj.title
            tailr_title = taistyle_obj.title
            total_meters = obj.total_meters

            return JsonResponse({"success": "Succesfully measure noted", 'data':{'order':order_obje,
                                        'customer':customer_obj,'comp_ordr_obj':order_obje,
                                         'fab_title':fab_title,'tailr_title':tailr_title,
                                         'total_meters':total_meters }}, status=200)
        except Exception as error:
            print("exception ===========>",error)
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
            return JsonResponse({"success": "Succesfully created order", 'data':{"order_id":complete_order_obj.pk}}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
