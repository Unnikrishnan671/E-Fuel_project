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
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'SuperAdmin_home')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="active").exists():
        
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Own_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                return render(request,'Owner_home.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="resign").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['usr_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'User_home.html',{'mem1':mem1})
        else:
            return render(request, 'login.html')
    return render(request,'login.html')




def Registration(request):
    if request.method == 'POST':
        acc = user_registration()
        acc.fullname = request.POST['name']
        acc.pincode = request.POST['pincode']
        acc.district = request.POST['district']
        acc.state = request.POST['state']
        acc.country = request.POST['country']
        acc.mobile = request.POST['mobile']
        acc.email = request.POST['email']
        acc.password = request.POST['password']
        acc.save()
    return render(request,'login.html')

def SuperAdmin_logout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/')

######################## Owner Section ######################

def Owner_index(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_index.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_home(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_home.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_addcategory(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            c_name=request.POST['c_name']
            addcategory=category(category_name=c_name
                                 )
            addcategory.save()
            return render(request, 'Owner_addcategory.html')
        return render(request,'Owner_addcategory.html')
    else:
        return redirect('/')

def Owner_addbunk(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            current_id = request.session['Own_id'] 
            b_name = request.POST['bunkname']
            vtype =request.POST.get('vehicletype')
            contrs =request.POST.get('connector')
            email = request.POST['email']
            ph = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            country = request.POST['country']
            img=request.FILES.get('file')
            addbunk=bunk(owner_ide=current_id,
                         bunk_name=b_name,
                         vehicle_type=vtype,
                         connector=contrs,
                         email=email,
                         phone=ph,
                         address=address,
                         city=city,
                         state=state,
                         country=country,
                         pincode=pincode,
                         image=img)
            addbunk.save()
            return render(request, 'Owner_addbunk.html',{'mem':mem})
        return render(request,'Owner_addbunk.html')
    else:
        return redirect('/')

def Owner_view_booking(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_view_booking.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_contact(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_contact.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_addproduct(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        categorys=category.objects.all()
        return render(request,'Owner_addproduct.html',{'mem':mem,'categorys':categorys})
    else:
        return redirect('/')
    
def Owner_addpro(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            p_name = request.POST['p_name']
            sel1 = request.POST['sel']
            category1=category.objects.get(id=sel1)
            desc=request.POST['description']
            price=request.POST['price']
            img=request.FILES.get('file')
            addproduct=Product(product_name=p_name,
                               product_image=img,
                               price=price,
                               description=desc,
                               category=category1
                               )
            addproduct.save()
            return render(request, 'Owner_addproduct.html')
        return render(request, 'Owner_view_product.html')
    else:
        return redirect('/')

def Owner_view_product(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        products=Product.objects.all()
        return render(request,'Owner_view_product.html',{'mem':mem,'products':products})
    else:
        return redirect('/')

def Owner_product_edit(request,p_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        products=Product.objects.get(id=p_id)
        return render(request,'Owner_product_edit.html',{'mem':mem,'products':products})
    else:
        return redirect('/')

def edit_product_details(request,products_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            products = Product.objects.get(id=products_id)
            products.product_name = request.POST.get('p_name')
            products.description = request.POST.get('description')
            products.price = request.POST.get('price')
            products.product_image = request.FILES.get('file')
            products.save()
            return redirect('Owner_view_product')
        return render(request, 'Owner_product_edit.html')
    else:
        return redirect('/')
def delete_product(request,p_id):
    products=Product.objects.get(id=p_id)
    products.delete()
    return redirect('Owner_view_product')

def Owner_logout(request):
    if 'Own_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

##################### Owner Section end #########################

##################### User Section Start ########################

def User_index(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_index.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_home(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_home.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_about(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_about.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_allbunk(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        bunks=bunk.objects.all()
        return render(request,'User_allbunk.html',{'mem1':mem1,'bunks':bunks})
    else:
        return redirect('/')

def book_bunk(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        if request.method=='POST':
            nam=request.POST['u_name']
            em=request.POST['email']
            ph=request.POST['phone']
            u_vtype=request.POST['v_type']
            u_vconnector=request.POST['c_type']
            da=request.POST['date']
            ti=request.POST['time']
            addbunkbook=bunk_booked(user_ide=usr_id,
                                 name=nam,
                                 email=em,
                                 phone=ph,
                                 uservehicle_type=u_vtype,
                                 userconnector=u_vconnector,
                                 date=da,
                                 time=ti
                                 )
            addbunkbook.save()
            print('save')
            return redirect('User_booking')
        return render(request,'User_mybooking.html')
    else:
        return redirect('/')

def User_contact(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_contact.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_shop(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_shop.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_addcart(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_addcart.html',{'mem1':mem1})
    else:
        return redirect('/')


def User_booking(request,i_id):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        book=bunk.objects.get(id=i_id)
        return render(request,'User_booking.html',{'mem1':mem1,'book':book})
    else:
        return redirect('/')

def User_mybooking(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_mybooking.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_payment_history(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_payment_history.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_logout(request):
    if 'usr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

###################### User section end ########################

###################### Super Admin section start ###############

def SuperAdmin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_index.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_home(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_home.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_bunkrequest(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_bunkrequest.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_bunkbookings(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_bunkbookings.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_ownerview(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_ownerview.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_userview(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_userview.html',{'users':users})
    else:
        return redirect('/')

###################### Super Admin section end ###############