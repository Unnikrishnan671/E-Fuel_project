from django.shortcuts import render

import os
import random
from django.shortcuts import render, redirect
from efuelapp.models import *
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.db.models import Q
# from efuel.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail


# Create your views here.
def login(request):
    return render(request,'login.html')

def Owner_index(request):
    return render(request,'Owner_index.html')

def Owner_home(request):
    return render(request,'Owner_home.html')

def Owner_addbunk(request):
    return render(request,'Owner_addbunk.html')

def Owner_view_booking(request):
    return render(request,'Owner_view_booking.html')

def Owner_contact(request):
    return render(request,'Owner_contact.html')

def Owner_addproduct(request):
    return render(request,'Owner_addproduct.html')

def Owner_view_product(request):
    return render(request,'Owner_view_product.html')

def Owner_product_edit(request):
    return render(request,'Owner_product_edit.html')

def User_index(request):
    return render(request,'User_index.html')

def User_home(request):
    return render(request,'User_home.html')

def User_about(request):
    return render(request,'User_about.html')

def User_allbunk(request):
    return render(request,'User_allbunk.html')

def User_contact(request):
    return render(request,'User_contact.html')

def User_shop(request):
    return render(request,'User_shop.html')

def User_addcart(request):
    return render(request,'User_addcart.html')


def User_booking(request):
    return render(request,'User_booking.html')

def User_mybooking(request):
    return render(request,'User_mybooking.html')

def User_payment_history(request):
    return render(request,'User_payment_history.html')

def SuperAdmin_index(request):
    return render(request,'SuperAdmin_index.html')

def SuperAdmin_home(request):
    return render(request,'SuperAdmin_home.html')

def SuperAdmin_bunkrequest(request):
    return render(request,'SuperAdmin_bunkrequest.html')

def SuperAdmin_bunkbookings(request):
    return render(request,'SuperAdmin_bunkbookings.html')

def SuperAdmin_ownerview(request):
    return render(request,'SuperAdmin_ownerview.html')

def SuperAdmin_userview(request):
    return render(request,'SuperAdmin_userview.html')