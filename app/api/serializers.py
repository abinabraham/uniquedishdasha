from django.db import models
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app.accounts.models import CustomUser, Branch
from app.orders.models import OrderBook, Orders

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name',]

class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'email', \
                'phone_number', "address"]

class OrderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = ["id","branch","total_meters","quantity","deliver_at",]

class CompleteOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id","total_amnt_to_pay","total_paid_amount","balance_amount","order_status",
                    "payment_status"]