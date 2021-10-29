from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app.accounts.models import CustomUser, Branch
from django.http import JsonResponse, HttpResponseBadRequest
from app.api.serializers import UserSerializer, UserAllSerializer, \
                                                OrderBookSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import (OrderBook, FabricType,
                     TailoringStyle )

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


@csrf_exempt
def order_ajaxcreaion(request):
    # request should be ajax and method should be POST.
    print("-----------------",request.POST)      
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
            customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
            return JsonResponse({"success": "Succesfully order booked", 'data':{'data':order_obj,'user':customer_obj,
                                                            'branch_title':branch_obj.title}}, status=200)
        except Exception as error:
            return JsonResponse({"error": error}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')



        


