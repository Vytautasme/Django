from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from .models import Country, City
from .forms import NameForm, forms


def countries(request):
    countries_list = Country.objects.all()
    context = {'countries': countries_list}
    return render(request, 'country/countries.html', context)


def country_add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            country = form['country'].value()
            population = form['population'].value()
            continent = form['continent'].value()
            obj = Country(country=country, population=population, continent=continent)
            obj.save()
            return redirect('countries:countries')

    else:
        form = NameForm()
    context = {'form': form}
    return render(request, 'country/country_add.html', context)

def delete_country(request, country_name):
    if request.method == "POST":
        country = Country.objects.get(country=country_name)
        country.delete()
        return redirect("countries:countries")
    context = {'country': country_name}
    return render(request, 'country/country_delete.html', context)

class CountryView(generic.ListView):
    template_name = "country/countries.html"
    context_object_name = "countries"

    def get_queryset(self):
        return Country.objects.all()


def country_view(request, country_name):
    country = get_object_or_404(Country, country=country_name)
    context = {'country': country}
    return render(request, 'country/countries_cities.html', context)


class CountryResultsView(generic.DetailView):
    model = Country
    template_name = "country/countries_cities.html"

    def get_object(self, queryset=None):
        country = get_object_or_404(Country, country=self.kwargs.get("country"))
        return country


def country_vote(request, country_name):
    country = get_object_or_404(Country, country=country_name)
    try:
        selected_choice = country.city_set.get(pk=request.POST["choice"])
    except(KeyError, Country.DoesNotExist):
        context = {"country": country,
                   "error_message": "You didn't select a choice.",
                   }
        return render(request, "country/country.html", context=context)
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("countries:country_view", args=(country.country,)))


def cities(request):
    cities_list = City.objects.all()
    context = {'cities': cities_list, 'country':'all', 'population':0}
    return render(request, "country/cities.html", context)


def get_cities_population_more_than(request, city_population):
    bigger_cities = City.objects.filter(city_population__gte=city_population)
    context = {'cities': bigger_cities, 'population': city_population}
    return render(request, "country/cities.html", context)


def filter_cities_by_country(request, country_name):
    country = Country.objects.get(country=country_name)
    cities_by_country = City.objects.filter(country=country)
    context = {'cities': cities_by_country}
    return render(request, "country/cities.html", context)


def filter_by_country_and_population(request, country_name, city_population):
    if country_name == "all":
        cities = City.objects.filter(city_population__gte=city_population)
    else:
        country = Country.objects.get(country=country_name)
        cities = City.objects.filter(country=country, city_population__gte=city_population)
    context = {'cities': cities,'country':country_name}
    return render(request, "country/cities.html", context)
