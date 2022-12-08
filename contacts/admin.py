from django.contrib import admin

# Register your models here.
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'LastName', 'email', 'car_tital', 'city', 'created_date')
    list_display_links = ('id', 'FirstName')
    search_fields = ('FirstName', 'LastName', 'email', 'car_tital')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
