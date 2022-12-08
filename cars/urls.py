from django.urls import path
from cars import views

urlpatterns = [
    path('', views.cars, name="cars"),
    path('search', views.search, name='search'),
    path('car_details/<int:id>', views.car_details, name='car_details'),
    # path("<car_id>/car_details/", views.car_details, name='car_details')
]
