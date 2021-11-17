
# Author: Abin Abraham 
# -*- coding: utf-8 -*-
# Order related models will adde here

import uuid
import random
import string

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords
from datetime import datetime
from core.utils import id_generator

from app.accounts.models import CustomUser, Branch

class FabricType(models.Model):
    help = "Fabric Type"
    title = models.CharField("Fabric Title", max_length=50,null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Fabric Type"
        verbose_name = "Fabric Types"

class TailoringStyle(models.Model):
    help = "Tailoring Style"
    title = models.CharField("Tailoring Title", max_length=50,null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Tailoring Style"
        verbose_name = "Tailoring Style"




class PricingPlans(models.Model):
    help = "Pricing Plans"
    tailr_styl = models.ForeignKey(TailoringStyle, on_delete=models.CASCADE,related_name="tailr_styl_payment"
                                             , null=True, blank=True)
    amount = models.DecimalField("Single Order Amount", max_digits=5, decimal_places=2, default=0)
    country = CountryField(default="KW")
    is_active = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.tailr_styl.title)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Pricing plans"
        verbose_name = "Pricing plans"




class PricingPlansFabricTyp(models.Model):
    help = "Pricing Plans Fabric Type"
    fabr_typ = models.ForeignKey(FabricType, on_delete=models.CASCADE,related_name="fabr_type_payment"
                                             , null=True, blank=True)
    amount = models.DecimalField("Single Order Amount", max_digits=5, decimal_places=2, default=0)
    country = CountryField(default="KW")
    is_active = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fabr_typ.title)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Pricing Plans Fabric Type"
        verbose_name = "Pricing Plans Fabric Type"

class Collars(models.TextChoices):
    COLLAR1 = 'C1', 'Collar1'
    COLLAR2 = 'C2', 'Collar2'
    COLLAR3 = 'C3', 'Collar3'
    COLLAR4 = 'C4', 'Collar4'
    POCKET1 = 'P1', 'Pocket1'
    POCKET2 = 'P2', 'Pocket2'
    POCKET3 = 'P3', 'Pocket3'
    POCKET4 = 'P4', 'Pocket4'
    ZIP1 = 'Z1', 'Zip1'
    ZIP2 = 'Z2', 'Zip2'
    ZIP3 = 'Z3', 'Zip3'
    ZIP4 = 'Z4', 'Zip4'


class Zips(models.TextChoices):
    ZIP1 = 'Z1', 'Zip1'
    ZIP2 = 'Z2', 'Zip2'
    ZIP3 = 'Z3', 'Zip3'
    ZIP4 = 'Z4', 'Zip4'

class Pockets(models.TextChoices):
    POCKET1 = 'P1', 'Pocket1'
    POCKET2 = 'P2', 'Pocket2'
    POCKET3 = 'P3', 'Pocket3'
    POCKET4 = 'P4', 'Pocket4'

class PocketsTwo(models.TextChoices):
    POCKETTWO1 = 'P21', 'PocketTwo1'
    POCKETTWO2 = 'P22', 'PocketTwo2'
    POCKETTWO3 = 'P23', 'PocketTwo3'
    POCKETTWO4 = 'P24', 'PocketTwo4'
    POCKETTWO5 = 'P25', 'PocketTwo5'
    POCKETTWO6 = 'P26', 'PocketTwo6'

class Tie(models.TextChoices):
    TIE1 = 'T1', 'Tie1'
    TIE2 = 'T2', 'Tie2'
    TIE3 = 'T3', 'Tie3'
    TIE4 = 'T4', 'Tie4'
    TIE5 = 'T5', 'Tie5'
    TIE6 = 'T6', 'Tie6'
    TIE7 = 'T7', 'Tie7'
    TIE8 = 'T8', 'Tie8'
    TIE9 = 'T9', 'Tie9'

class PenPocket(models.TextChoices):
    PENPOCKET1 = 'PP1', 'PenPocket1'
    PENPOCKET2 = 'PP2', 'PenPocket2'
    PENPOCKET3 = 'PP3', 'PenPocket3'
    PENPOCKET4 = 'PP4', 'PenPocket4'
    PENPOCKET5 = 'PP5', 'PenPocket5'
    PENPOCKET6 = 'PP6', 'PenPocket6'

class Cufflink(models.TextChoices):
    CUFFLINK1 = 'CL1', 'Cufflink1'
    CUFFLINK2 = 'CL2', 'Cufflink2'
    CUFFLINK3 = 'CL3', 'Cufflink3'
    CUFFLINK4 = 'CL4', 'Cufflink4'
    CUFFLINK5 = 'CL5', 'Cufflink5'
    CUFFLINK6 = 'CL6', 'Cufflink6'
    CUFFLINK7 = 'CL7', 'Cufflink7'
    CUFFLINK8 = 'CL8', 'Cufflink8'

class InsidePocketShape(models.TextChoices):
    INSIDEPOCKETSHAPE1 = 'IPS1', 'InsidePocketShape1'
    INSIDEPOCKETSHAPE2 = 'IPS2', 'InsidePocketShape2'

class Buttons(models.TextChoices):
    BUTTON1 = 'BTN1', 'Button1'
    BUTTON2 = 'BTN2', 'Button2'


class FinalStyle(models.TextChoices):
    FINALSTYLE1 = 'FS1', 'FinalStyle1'
    FINALSTYLE2 = 'FS2', 'FinalStyle2'

class Line(models.TextChoices):
    LINE1 = 'OneLine', 'OneLine'
    LINE2 = 'TwoLine', 'TwoLine'


class Measurements(models.Model):
    help = "Measurements"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measure_id = models.CharField("Measurement ID",null=True, blank=True, max_length=100)
    collar = models.CharField(
                        max_length=2,
                        choices=Collars.choices,
                        default=Collars.COLLAR1,
                    )
    zip = models.CharField(
                        max_length=2,
                        choices=Zips.choices,
                        default=Zips.ZIP1,
                        null=True, blank=True,
                    )
    pocket = models.CharField(
                        max_length=2,
                        choices=Pockets.choices,
                        default=Pockets.POCKET1,
                        null=True, blank=True,
                    )
    pockettwo = models.CharField(
                        max_length=5,
                        choices=PocketsTwo.choices,
                        default=PocketsTwo.POCKETTWO1,
                    )
    tie = models.CharField(
                        max_length=5,
                        choices=Tie.choices,
                        default=Tie.TIE1,
                    )
    penpocket = models.CharField(
                        max_length=5,
                        choices=PenPocket.choices,
                        default=PenPocket.PENPOCKET1,
                    )
    
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sholderOne = models.CharField("Shoulder One", max_length=50,null=True, blank=True)
    sholderTwo = models.CharField("Shoulder Two", max_length=50,null=True, blank=True)
    mainWidth = models.CharField("Main Width", max_length=50,null=True, blank=True)
    penPocket_select = models.CharField("Pen Pocket", max_length=50,null=True, blank=True)
    insidePocket = models.CharField("Inside Pocket", max_length=50,null=True, blank=True)
    handSize = models.CharField("Hand Size", max_length=50,null=True, blank=True)

    cufflink = models.CharField(
                        max_length=5,
                        choices=Cufflink.choices,
                        default=Cufflink.CUFFLINK1,
                    )
    insidepocketshape = models.CharField(
                        max_length=5,
                        choices=InsidePocketShape.choices,
                        default=InsidePocketShape.INSIDEPOCKETSHAPE1,
                    )
    button = models.CharField(
                        max_length=5,
                        choices=Buttons.choices,
                        default=Buttons.BUTTON1,
                    )
    finalstyle = models.CharField(
                        max_length=5,
                        choices=FinalStyle.choices,
                        default=FinalStyle.FINALSTYLE1,
                    )

    width_collar = models.CharField("Width Collar", max_length=50,null=True, blank=True)
    size_collar = models.CharField("Size Collar", max_length=50,null=True, blank=True)
    shoulder = models.CharField("Size Collar", max_length=50,null=True, blank=True) 
    front_chest = models.CharField("Front Chest", max_length=50,null=True, blank=True) 
    bar = models.CharField("Bar", max_length=50,null=True, blank=True) 
    sleeve_length = models.CharField("Sleeve Length", max_length=50,null=True, blank=True) 
    front_pocket = models.CharField("Front Pocket", max_length=50,null=True, blank=True) 
    size_pocket = models.CharField("Size Pocket", max_length=50,null=True, blank=True)
    big_pocket = models.CharField("Big Pocket", max_length=50,null=True, blank=True) 
    fold_width = models.CharField("Fold Width", max_length=50,null=True, blank=True) 
    fold_length =  models.CharField("Fold Length", max_length=50,null=True, blank=True) 
    two_line = models.CharField("Two Line", max_length=50,null=True, blank=True) 
    length = models.CharField("Front Length", max_length=50,null=True, blank=True) 
    back_length = models.CharField("Back Length", max_length=50,null=True, blank=True) 


    fb_type = models.ForeignKey(FabricType, on_delete=models.CASCADE,related_name="fbrc_typ"
                                             , null=True, blank=True)
    tailr_styl = models.ForeignKey(TailoringStyle, on_delete=models.CASCADE,related_name="tailr_styl"
                                             , null=True, blank=True)
    color = models.CharField("Color", max_length=50,null=True, blank=True)
    total_meters = models.CharField("Total Meters", max_length=50,null=True, blank=True)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2, default=0)
    
    line = models.CharField(
                        max_length=10,
                        choices=Line.choices,
                        default=Line.LINE1,
                        null=True, blank=True,
                    )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Measurement"
        verbose_name = "Measurements"

    
    def save(self, *args, **kwargs):
        self.measure_id=id_generator()
        super(Measurements, self).save(*args, **kwargs)


class OrderStatus(models.TextChoices):
    ORDERED = 'OS1', 'Ordered' #Created New order
    COMPLETED = 'OS2', 'COMPLETED' #Tailoring COmpleted
    DELIVERED = 'OS3', 'DELIVERED' #Delivered and dispatched


class PaymentStatus(models.TextChoices):
    NOTPAID = 'PS1', 'NOT PAID' 
    PARTPAID = 'PS2', 'PARTIALLY PAID'
    PAID = 'PS3', 'FULLY PAID'
    OVERPAID = 'PS4', 'OVERPAID'

class PaymentMethod(models.TextChoices):
    CASH = 'PM1', 'CASH' #Cash
    CREDITCARD = 'PM2', 'CREDIT CARD' #CC
    DEBITCARD = 'PM3', 'DEBIT CARD' #DC
    PAYLATER = 'PM4', 'PAY LATER' #PL




class Orders(models.Model):
    help = "Orders"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField("Order ID",null=True, blank=True, max_length=100)

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name="order_branch"
                                          , null=True, blank=True)
    is_customer_own_fabric = models.BooleanField(default=True)

    quantity = models.CharField("Quantity", max_length=50,null=True, blank=True)
    deliver_at = models.DateTimeField()
    delivered_date = models.DateTimeField(null=True, blank=True)
    measurements = models.ManyToManyField(Measurements)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="main_order_customer")
    total_amnt_to_pay = models.DecimalField("Total Amount to Pay", max_digits=5, decimal_places=2,  default=0)
    total_paid_amount = models.DecimalField("Total Amount Paid", max_digits=5, decimal_places=2, default=0)
    balance_amount = models.DecimalField("Balance Amount", max_digits=5, decimal_places=2, default=0)

    order_status = models.CharField(
                        max_length=5,
                        choices=OrderStatus.choices,
                        default=OrderStatus.ORDERED,
                    )
    payment_status = models.CharField(
                        max_length=5,
                        choices=PaymentStatus.choices,
                        default=PaymentStatus.NOTPAID,
                    )

    payment_method = models.CharField(
                        max_length=5,
                        choices=PaymentMethod.choices,
                        default=PaymentMethod.CASH,
                    )


    history = HistoricalRecords()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Complete Order"
        verbose_name = "Complete Order"

    
    def save(self, *args, **kwargs):
        self.order_id=id_generator()
        super(Orders, self).save(*args, **kwargs)

