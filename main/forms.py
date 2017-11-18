# -*- coding: utf-8 -*-

from .models import *
from django import forms
from django.utils.translation import gettext as _

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = "__all__"

class ViolationForm(forms.ModelForm):
    class Meta:
        model = Violation
        fields = "__all__"

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        exclude = ['user','car','violation_number']

        widgets = {
        'date': forms.DateTimeInput(attrs={'type':'date'}),

        }
        labels = {
            'date': _(' تاريخ المخالفة'),
            'violation': _(' نوع المخالفة'),
            'car_number': _(' رقم السيارة'),
            'response': _(' أقوال المخالف'),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    labels = {
        'username': _(' رمز الدخول'),
        'violation_number': _(' كلمة السر'),
    }
