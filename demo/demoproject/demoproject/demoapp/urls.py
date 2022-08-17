from .import views
from django.urls import path

urlpatterns = [
    path('',views.details,name="details"),
    #path('', views.about, name="about"),python m
    #path('add/',views.calculate,name="calculate"),

    #path('sub/',views.subtraction,name="subtraction"),
    #path('mult/',views.multiplication,name="multiplication"),
    #path('divide/',views.division,name="division")
    #path('contact/',views.contact,name="contact"),
    #path('details/',views.details,name="details"),
    #path('thanks/',views.thanks,name="thanks")
    #path('about/add/',views.addition,name="addition")
    #path('add/calculate/',views.calculate, name="calculate")
]
