from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50px" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car image'

    list_display = ('id', 'thumbnail', 'car_Tital', 'city', 'year', 'is_featured')
    list_display_links = ('id', 'car_Tital')
    search_fields = ('id', 'car_Tital', 'city', 'model')
    list_filter = ('city', 'model')
    list_editable = ('is_featured',)


admin.site.register(Car, CarAdmin)
