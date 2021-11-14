
# Author: Abin Abraham 
# -*- coding: utf-8 -*-
# Accounts related models will adde here

import uuid
import random
import string

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField
from datetime import datetime

from core.utils import id_generator

USER_TYPES = (
    (0, 'SuperAdmin'),
    (1, 'Branch Admin'), #Staff
    (2, 'Customer'), #Customer
)

class Branch(models.Model):
    help = "Branch Table"
    country = CountryField(default="KW")
    title = models.CharField("Branch Name", max_length=50,null=True, blank=True)
    address = models.TextField("Address",null=True, blank=True)   


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Branch"
        verbose_name = "Branches"


class CustomUser(AbstractUser):
    """
    add custom User fields here
    example: profile pic, dob, address
    I'm just make this with pass statment
    for the updation later on Profile Fields
    must include UserManager() as object
    """
    help = "User Table"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField("User ID",null=True, blank=True, max_length=100)
    role_name = models.PositiveSmallIntegerField(choices=USER_TYPES, default=1)
    country = CountryField(default="KW")
    phone_number = models.CharField("Phone Number",null=True, blank=True, max_length=100)
    place = models.CharField("Place",null=True, blank=True, max_length=100)
    area = models.CharField("Area",null=True, blank=True, max_length=100)
    address = models.TextField("Address",null=True, blank=True)   
    notes = models.TextField("Notes",null=True, blank=True)    
    balance = models.DecimalField("Wallet Balance", max_digits=5, decimal_places=2, default=0)

    
    is_verified = models.BooleanField(default=False)
    is_profile_completed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) #means role=1


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%y%m%d', blank=True, default='/static/images/user.png')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name="branch"
                                , null=True, blank=True)


    def __str__(self):
        if self.first_name and self.last_name and self.phone_number:
            return self.first_name + " " + self.last_name + " (" + self.phone_number + ")"
        else:
            return self.username

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = "User"
        verbose_name = "Users"
    

    
    def save(self, *args, **kwargs):
        first_name = self.first_name.split(' ')[0]
        last_name = self.first_name.split(' ')[0]

        self.user_id=str(id_generator())
        if not self.username:
            self.username=str(id_generator())
        self.role_name = 2
        if not self.first_name:
            self.first_name = first_name
        if not self.last_name:
            self.last_name = last_name
        if not self.user_id:
            self.user_id = self.user_id
        if not self.__class__.objects.filter(phone_number=self.phone_number):
            super(CustomUser, self).save(*args, **kwargs)