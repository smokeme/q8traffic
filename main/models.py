# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext as _
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cars(models.Model):
    number = models.IntegerField()
    owner = models.CharField(max_length=200)
    email = models.EmailField(max_length=340)

    def __str__(self):
        return "%s" % self.number

STATUS_CHOICES = (
    (1, _("1 year")),
    (2, _("3 months")),
    (3, _("6 months")),
    (4, _("1 month")),
    (5, _("15 days")),
    (6, _("None"))
)
class Violation(models.Model):
    type = models.IntegerField()
    desc = models.CharField(max_length=500)
    amount = models.IntegerField()
    ticket_price = models.IntegerField()
    points = models.IntegerField(default=0)
    detention = models.IntegerField(choices=STATUS_CHOICES, default=6)

    def __str__(self):
        return self.desc

class Ticket(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    violation = models.ForeignKey(Violation,blank=True,null=True)
    car = models.ForeignKey(Cars,blank=True,null=True)
    car_number = models.IntegerField()
    violation_number = models.IntegerField(null=True,blank=True)
    response = models.CharField(max_length=500)

    def __str__(self):
        return "%s - Violation for car - %s " %(self.violation,self.car)
