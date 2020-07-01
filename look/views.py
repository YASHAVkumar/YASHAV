from django.shortcuts import render,HttpResponse,redirect
import uuid
from django.db import connection
from django.contrib.auth.models import User,auth
# Create your views here.
from .models import mark,kitchen,detail,product,total_product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View



name = "user"
def login(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        passwd = request.POST.get('pas')
        cpassword = request.POST.get('pas1')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('add')
        if (passwd == cpassword):
            user = User.objects.create_user(username=uname, password=passwd, email=email, first_name=fname,
                                                last_name=lname)
            user.save()
            obj = detail()
            obj.fname = fname
            obj.lname = lname
            obj.uname = uname
            obj.password = passwd
            obj.email = email
            obj.phone = phone
            obj.address = address
            obj.save()
            print("user is created")
            return render(request, 'login.html')
        else:
            var = "Your passwords is matched Try again"
            return render(request, 'sign_up.html', {'var': var})
    return render(request, 'login.html')

def index(request):
    uname=request.GET.get("user")

    print(uname)
    objs = kitchen.objects.all()
    order = total_product.objects.all()

    off = 72
    allprod=[]
    objs=total_product.objects.values('product_cat','product_uid')
    cats={item['product_cat'] for item in objs }
    for cat in cats:
        prod=total_product.objects.filter(product_cat=cat)
        allprod.append([prod])
    count=0
    #for i in allprod:
     #   for j in i:
      #      for k in j:
       #         print(k.product_name)

    return render(request, 'index.html', {'products': order, 'off': off,'allprod':allprod})

def sign(request):
    return render(request, 'sign_up.html')

def contact(request):
    if (request.method == "get"):
        var = request.GET.get("feedback")
        print("this ", var)
        return redirect('contact')
    return render(request, "contact.html")


def gold(request):
    if (request.method == 'GET'):
        uname = request.GET.get('user')
        passwd = request.GET.get('password')
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            if user.is_active:
                print("hi")
                login(request)

                objs = kitchen.objects.all()
                order = total_product.objects.all()

                mark = 1
                allprod = []
                objs = total_product.objects.values('product_cat', 'product_uid')
                cats = {item['product_cat'] for item in objs}
                for cat in cats:
                    prod = total_product.objects.filter(product_cat=cat)
                    allprod.append([prod])
                count = 0
                # for i in allprod:
                #   for j in i:
                #      for k in j:
                #         print(k.product_name)
                if user.is_staff:
                    o=1
                else:
                    o=0

                return render(request, 'index.html', {'name': uname, 'products': order, 'off': mark, 'allprod': allprod,'staff':o})

        elif user is None:
            messages.warning(request, 'No login Details are found in system.Register yourself')
            return redirect('login')

from django.db import connection
from collections import namedtuple
def search(request):
    var = request.GET.get("text")
    print(var)
    str=var+'%'

    row= total_product.objects.raw("select * from look_total_product where product_name like %s",[str])

    return render(request, 'search.html',{'row':row})

def cart(request):
    allprod = []
    objs = total_product.objects.values('product_cat', 'product_uid')
    cats = {item['product_cat'] for item in objs}
    for cat in cats:
        prod = total_product.objects.filter(product_cat=cat)
        allprod.append([prod])
    return render(request,'shop_cart.html',{'allprod':allprod})


def pay(request):
    return HttpResponse("This is Payment corner For our Website Let See")
