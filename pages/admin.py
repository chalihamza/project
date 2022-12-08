from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from pages.models import Team


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style=" border-radius:40px "/>'.format(object.image.url))
    thumbnail.short_description = 'photo'
    list_display = ('id', 'thumbnail', 'Designation', 'date')
    list_display_links = ('id',)
    list_filter = ('Designation',)
    search_fields = ('FirstName', 'Designation')


admin.site.register(Team, TeamAdmin)
