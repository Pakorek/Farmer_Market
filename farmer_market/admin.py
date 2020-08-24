from django.contrib import admin

from .models import City, Market, NbFarmer


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept')
    list_filter = ('dept', )
    ordering = ('name', )
    search_fields = ('name', 'dept')


class MarketAdmin(admin.ModelAdmin):
    list_display = ('place', 'city_id', 'day', 'nb_farmers_id')
    list_filter = ('city_id', 'day', )
    ordering = ('day', 'city_id', )
    search_fields = ('place', 'city_id', 'day')


admin.site.register(City, CityAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(NbFarmer)
