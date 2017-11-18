# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import requests
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
            try:
                car = Cars.objects.get(number=car_number)
            except:
                return redirect('/')
            ticket.car = car
            ticket.user = request.user
            x = ticket.save()
            y = send_simple_message(car.email,ticket.id)
            print(y)
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

def ticket_detail(request, myid):
    if not request.user.is_authenticated():
        return redirect("login")
    instance = get_object_or_404(Ticket, id=myid)
    context = {
    "object": instance,
    }
    return render(request, 'detail.html', context)


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

def send_simple_message(email, id):
    return requests.post(
        "https://api.mailgun.net/v3/mg.fawaz.online/messages",
        auth=("api", "key-0d80529bad46a5391564b02447d65732"),
        data={"from": "Q8 Traffic <mailgun@fawaz.online>",
              "to": [email],
              "subject": "Q8 Traffic",
              "text": "New violation, to check the ticket click on the following link http://fawaz.online/check/%s" % (id)})
