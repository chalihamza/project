from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.forms import CharField


# Create your models here.


class Car(models.Model):
    state_choice = (
        ('PU', 'punjab'),
        ('KPK', 'khyber pukhtankhwa'),
        ('BL', 'blochistan'),
        ('FD', 'fedral Territory'),
        ('SN', 'sindh'),
        ('KS', 'kashmir'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choice = (
        ('Cruise control', 'Cruise control'),
        ('Audio interface', 'Audio interface'),
        ('Airbags', 'Airbags'),
        ('Air condition', 'Air condition'),
        ('seat heating', 'seat heating'),
        ('Alram system', 'Alram system'),
        ('parkassist', 'parkassist'),
        ('power steering', 'power steering'),
        ('revers camera', 'revers camera'),
        ('Direct fuel injection', 'Direct fuel injection'),
        ('Auto start/stop', 'Auto start/stop'),
        ('wind deflector', 'wind deflector'),
        ('Bluetooth handset', 'Bluetooth handset'),
        # ('Burmester Surround Sound', 'Burmester Surround Sound')
        # ('Wind Deflector', 'Wind Deflector')
        # ('Universal Audio Interface', 'Universal Audio Interface')
        # ('Anti-theft Protection', 'Anti-theft Protection')
        # ('Automatic Climate Control', 'Automatic Climate Control')

    )
    door_choice = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    car_Tital = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=300)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField('year', choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    discreption = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    features = models.CharField(max_length=26,choices=features_choice)
    body_style = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    interior = models.CharField(max_length=200)
    miles = models.IntegerField()
    door = models.CharField(choices=door_choice, max_length=100)
    passangers = models.IntegerField()
    vin_no = models.CharField(max_length=200)
    millage = models.IntegerField()
    fule_type = models.CharField(max_length=100)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_Tital
