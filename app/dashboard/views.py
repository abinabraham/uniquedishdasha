from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from app.accounts.models import CustomUser
from django.db.models import Q
from django.contrib import messages
from app.api.serializers import UserSerializer

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
    data = UserSerializer(customers, context={'request': None}, 
                many=True,).data
    result = []
    for i, val in enumerate(data):
        result.append(val['first_name']+', ('+str(val['id'])+')')
    return json.dumps(result)