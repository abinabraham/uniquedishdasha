from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app.accounts.models import CustomUser
from django.http import JsonResponse
from app.api.serializers import UserSerializer, UserAllSerializer
from rest_framework.response import Response

class OrderView(FormView):
    template_name = "orders/orders_1.html"

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = {'redir':""}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
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

def order_ajaxsubmission(request):
    # request should be ajax and method should be POST.
    try:
        if request.is_ajax and request.method == "POST":
            step = request.POST.get('step')
            fields = ['first_name','last_name','email','address','place' \
                    'area','phone_number']
            data = {k:v for (k,v) in request.POST.items() if k in fields}
            data['username'] = request.POST.get('email')
            if step == "step1":
                try:
                    customer = CustomUser(**data).save()
                    customer_obj = CustomUser.objects.get(username=data['username'])
                    customer_obj = UserAllSerializer(customer_obj, context={'request': None}).data
                    return JsonResponse({"success": "Succesfully Saved customer", 'data':customer_obj}, status=200)
                except Exception as error:
                    return JsonResponse({"error": error}, status=400)
    except Exception as error:
       return JsonResponse({"error": error}, status=400)