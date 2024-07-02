from django.shortcuts import render
from .models import NavbarItem, AboutUs, Service

# Create your views here.

def home(request):
    navs = NavbarItem.objects.all()
    context = {'navs': navs}
    return render(request, 'core/home.html', context)

def about_us(request):
    navs = NavbarItem.objects.all()
    about_us_info = AboutUs.objects.all()
    context = {'navs': navs, 'about_us_info': about_us_info}
    return render(request, 'core/quienes.html', context)

def services(request):
    navs = NavbarItem.objects.all()
    services_list = Service.objects.all()
    context = {'navs': navs, 'services_list': services_list}
    return render(request, 'core/servicios.html', context)
