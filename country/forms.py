from django import forms
from django.forms import ModelForm

from country.models import Country

# class NameForm(forms.Form):
#     country = forms.CharField(label="Country name", max_length=100)
#     population = forms.IntegerField(label="Population")
#     continent = forms.CharField(label="Continent", max_length=100)


class NameForm(ModelForm):
    class Meta:
        model = Country
        fields = ["country", "population", "continent"]