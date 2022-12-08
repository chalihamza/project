from django.shortcuts import render

# Create your views here.
from cars.models import Car
from pages.models import Team
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    teams = Team.objects.all()
    all_cars = Car.objects.order_by('-created_date')
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)  # ya featured cares ke ha
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    model_city = Car.objects.values_list('city', flat=True).distinct()
    model_year = Car.objects.values_list('year', flat=True).distinct()
    model_body_style = Car.objects.values_list('body_style', flat=True).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_cars, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'teams': teams,
        'all_cars': users,
        'cars': cars,
        'model_search': model_search,
        'model_city': model_city,
        'model_year': model_year,
        'model_body_style': model_body_style,

    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')
