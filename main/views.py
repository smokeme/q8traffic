# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from decimal import Decimal
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def ticket_list(request):
    if not request.user.is_authenticated():
        return redirect("login")
    mylist = Ticket.objects.all() #.order_by("-timestamp","-updated")
    number = mylist.count()
    paginator = Paginator(mylist, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    context = {
    "mylist": objects,
    "number": number,
    }
    return render(request, 'ticket_list.html', context)

def create_ticket(request):
    context = {}
    if not request.user.is_authenticated():
        return redirect("login")
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            car_number = ticket.car_number
            violation_number = ticket.violation_number
            try:
                violation = Violation.objects.get(type=violation_number)
                car = Cars.objects.get(number=car_number)
            except:
                return redirect('/')
            ticket.car = car
            ticket.violation = violation
            ticket.user = request.user
            ticket.save()
            return redirect('/')
    context['form'] = form
    return render(request, 'create_ticket.html', context)

def about(request):
    if not request.user.is_authenticated():
        return redirect("login")
    context = {}
    return render(request, 'about.html', context)

def violation_list(request):
    if not request.user.is_authenticated():
        return redirect("login")
    mylist = Violation.objects.all() #.order_by("-timestamp","-updated")
    number = mylist.count()
    paginator = Paginator(mylist, 10) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    context = {
    "mylist": objects,
    "number": number,
    }
    return render(request, 'violation_list.html', context)


def mylogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('list')

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect("login")
		messages.error(request, form.errors)
		return redirect("login")
	return render(request, 'login.html', context)

def mylogout(request):
	logout(request)
	return redirect("login")
