from django.contrib import admin
from .models import Country, State, Currency, ExchangeRate

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Currency)
admin.site.register(ExchangeRate)