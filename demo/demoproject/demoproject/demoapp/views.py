from django.shortcuts import render
from django.http import HttpResponse
from .models import place,team


# Create your views here.
#def addition(request):
 #  name="india"
  # return render(request,"results.html",{'obj':r})








#def home(request):
 # return HttpResponse("hii home")
#def about(request):
 # return render(request,"about.html")
def details(request):
  obj=place.objects.all()
  obj1=team.objects.all()

  return render(request,"index.html",{'res':obj,'res1':obj1})
#def calculate(request):
 #  x=int(request.GET['n1'])
  # y=int(request.GET['n2'])
   #add =x+y
   #sub =x-y
   #mul =x*y
   #div =x/y
   #return render(request,"results.html",{"addition":add, "sub":sub, "mul":mul, "division":div})
#def thanks(request):
 #   return HttpResponse("Thanks")

