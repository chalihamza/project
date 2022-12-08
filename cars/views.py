from typing import Any

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    model_city = Car.objects.values_list('city', flat=True).distinct()
    model_year = Car.objects.values_list('year', flat=True).distinct()
    model_body_style = Car.objects.values_list('body_style', flat=True).distinct()

    page = request.GET.get('page', 1)

    paginator = Paginator(cars, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'cars': users,
        'model_search': model_search,
        'model_year': model_year,
        'model_city': model_city,
        'model_body_style': model_body_style,
    }
    return render(request, 'cars/cars.html', data)


def car_details(request, id):
    single_cars = Car.objects.get(id=id)
    print(id)
    data = {
        'single_cars': single_cars,
    }
    return render(request, 'cars/car_details.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    model_city = Car.objects.values_list('city', flat=True).distinct()
    model_year = Car.objects.values_list('year', flat=True).distinct()
    model_transmission = Car.objects.values_list('transmission', flat=True).distinct()
    model_body_style = Car.objects.values_list('body_style', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(discreption__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'model_year': model_year,
        'model_city': model_city,
        'model_body_style': model_body_style,
        'model_transmission': model_transmission,
    }
    return render(request, 'cars/search.html', data)
