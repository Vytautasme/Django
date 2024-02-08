from django.urls import path
from .views import (countries, cities, country_vote, CountryView, CountryResultsView, country_add, filter_by_country_and_population,
                    get_cities_population_more_than, filter_cities_by_country, country_view, delete_country)


app_name = "countries"

urlpatterns = [
    path("", countries, name='countries'),
    path("add", country_add, name='country_add'),
    path("<str:country_name>/delete", delete_country, name='delete_country'),
    path("cities", cities, name='cities'),
    path("cities/greater/<int:city_population>", get_cities_population_more_than, name='greater'),
    path("cities/<str:country_name>", filter_cities_by_country, name='by_country'),
    path("cities/<str:country_name>/greater/<int:city_population>", filter_by_country_and_population, name='by_country_and_pop'),
    path("", CountryView.as_view, name='countries'),
    path('<str:country_name>/vote', country_vote, name='countries_vote'),
    path('<str:country_name>/cities', country_view, name='country_cities'),
    path("<str:country>/results/", CountryResultsView.as_view(), name="country_view"),
]
