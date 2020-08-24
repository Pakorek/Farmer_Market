from django.contrib import admin

from .models import City, Market, NbFarmer


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept')
    list_filter = ('dept', )
    ordering = ('name', )
    search_fields = ('name', 'dept')


admin.site.register(City, CityAdmin)
admin.site.register(Market)
admin.site.register(NbFarmer)
