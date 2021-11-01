
# Author: Abin Abraham 
# -*- coding: utf-8 -*-
# Accounts related models will adde here


from django.db import models

class Colors(models.Model):
    help = "Color master Table"
    name = models.CharField("Color Name", max_length=50,null=True, blank=True)
    code = models.CharField("Color Code", max_length=50,null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Colors"
        verbose_name = "Colors"