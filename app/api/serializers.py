from django.db import models
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from app.accounts.models import CustomUser, Branch
from app.orders.models import Orders, Measurements

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
        fields = ['id','first_name','user_id']

class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'email', \
                'phone_number', "address", "user_id"]


class CompleteOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id","total_amnt_to_pay","total_paid_amount","balance_amount","order_status",\
                    "payment_status","order_id","quantity","deliver_at","customer"]

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ["id","width_collar","size_collar","measure_id","shoulder",\
                    "front_chest","bar","sleeve_length","front_pocket","size_pocket",\
                    "big_pocket", "fold_width","fold_length","two_line","length"]

