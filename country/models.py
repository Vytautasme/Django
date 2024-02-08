import datetime
from django.db import models
from django.forms import forms, Textarea
from django.utils.timezone import now
class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        abstract = True

class Country(BaseModel):
    continent_choices = {
        "europa":"Europe",
        "afrika":"Africa",
        "s_amerika": "North America",
        "p_amerika": "South America",
        "azija": "Asia",
        "australija":"Australia",
        "antarktida":"Antarctic"
    }
    country = models.CharField(max_length=50, unique=True)
    population = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=now)
    continent = models.CharField(max_length=50, choices=continent_choices)
    # description = models.CharField(widget=forms.Textarea)

    def __str__(self):
        return f'{self.country},   {str(self.population)}'

    def was_published_recently(self):
        return self.pub_date >= now() - datetime.timedelta(days=1)

class City(BaseModel):
    city = models.CharField(max_length=50)
    city_population = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.city},  {self.country.country}'
