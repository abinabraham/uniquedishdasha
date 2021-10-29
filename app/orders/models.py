
# Author: Abin Abraham 
# -*- coding: utf-8 -*-
# Order related models will adde here

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone

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


class OrderBook(models.Model):
    help = "Tailoring Style"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name="order_branch"
                                          , null=True, blank=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="order_customer")
    is_customer_own_fabric = models.BooleanField(default=True)
    fb_type = models.ForeignKey(FabricType, on_delete=models.CASCADE,related_name="fbrc_typ"
                                             , null=True, blank=True)
    tailr_styl = models.ForeignKey(TailoringStyle, on_delete=models.CASCADE,related_name="tailr_styl"
                                             , null=True, blank=True)
    color = models.CharField("Color", max_length=50,null=True, blank=True)
    total_meters = models.CharField("Total Meters", max_length=50,null=True, blank=True)
    quantity = models.CharField("Quantity", max_length=50,null=True, blank=True)
    deliver_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Order Book"
        verbose_name = "Order Book"