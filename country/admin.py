from django.contrib import admin
from .models import Country, City


class CountryAdmin(admin.ModelAdmin):
    list_display = ["country", "population", "continent", "pub_date"]


admin.site.register(Country, CountryAdmin)
admin.site.register(City)
