from django.shortcuts import render

# Create your views here.
from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    all_cars = Car.objects.order_by('-created_date')
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)  # ya featured cares ke ha
    data = {
        'teams': teams,
        'all_cars': all_cars,
        'cars': cars,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')
