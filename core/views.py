from django.shortcuts import render
from .models import NavbarItem, AboutUs, Service

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def about_us(request):
    about_us_info = AboutUs.objects.all()
    context = {'about_us_info': about_us_info}
    return render(request, 'core/about_us.html', context)

def services(request):
    services_list = Service.objects.all()
    context = {'services_list': services_list}
    return render(request, 'core/services.html', context)
