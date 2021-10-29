from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from app.accounts.models import CustomUser
from django.db.models import Q
from django.contrib import messages
from app.api.serializers import UserSerializer, UserAllSerializer

import json

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
            | Q(email__contains=term)
        )
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
        d['user_id'] = str(val['id'])

        d['label']= first_name+" "+last_name
        d['value']= first_name + " " + last_name +" -  (" +email+") - "+ phone 


        result.append(d)
        # result.append('<div class="resultData idData"><span>' +str(val['id'])+ '<div class="resultData nameData"><span>'+first_name+' '+last_name+'</span></div> <div class="resultData emailData"><span>'+email+'</span></div><div class="resultData phoneData"><span>'+phone+'</span></div> ')
    return json.dumps(result)


class DummyView(TemplateView):
    template_name = "dummy.html"