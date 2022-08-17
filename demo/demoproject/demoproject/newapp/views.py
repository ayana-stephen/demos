from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        u1=request.POST['username']
        f1= request.POST['firstname']
        l1 = request.POST['lastname']
        g1 = request.POST['email']
        p1 = request.POST['password']
        c1 = request.POST['cpassword']
        if p1==c1:
            if User.objects.filter(username=u1).exists():
              messages.info(request,"already used username")
              return redirect('register')
            elif User.objects.filter(email=g1).exists():
              messages.info(request,"already used email")
              return redirect('register')
            else:
             user=User.objects.create_user(username=u1,first_name=f1,last_name=l1,email=g1,password=p1)
             user.save();
             return redirect('login')

        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def login(request):
       if request.method=='POST':
           username=request.POST['username']
           password=request.POST['password']
           user=auth.authenticate(username=username,password=password)
           if user is not None:
               auth.login(request,user)
               return redirect('/')
           else:
               messages.info(request,"Invalid")
               return redirect('login')
       return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')