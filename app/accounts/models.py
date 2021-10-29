
# Author: Abin Abraham 
# -*- coding: utf-8 -*-
# Accounts related models will adde here

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField

USER_TYPES = (
    (0, 'SuperAdmin'),
    (1, 'Branch Admin'),
    (2, 'Branch User'), #Customer
)

class Branch(models.Model):
    help = "Branch Table"
    country = CountryField()
    title = models.CharField("Branch Name", max_length=50,null=True, blank=True)

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
    role_name = models.PositiveSmallIntegerField(choices=USER_TYPES, default=1)
    phone_number = models.CharField("Phone Number",null=True, blank=True, max_length=100)
    place = models.CharField("Place",null=True, blank=True, max_length=100)
    area = models.CharField("Area",null=True, blank=True, max_length=100)
    address = models.TextField("Address",null=True, blank=True)   
    notes = models.TextField("Notes",null=True, blank=True)    

    
    is_verified = models.BooleanField(default=False)
    is_profile_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%y%m%d', blank=True, default='/static/images/user.png')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,related_name="branch"
                                , null=True, blank=True)


    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "User"
        verbose_name = "Users"