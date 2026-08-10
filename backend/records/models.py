from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del País")
    iso_code = models.CharField(max_length=3, unique=True, help_text="Código ISO de 2 o 3 letras (ej. VE, US, MEX)", verbose_name="Código ISO")
    phone_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Código Telefónico", help_text="Ej. +58, +1")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['name']

    @property
    def country_label(self):
        return f"{self.name} ({self.iso_code})"

    def __str__(self):
        return f"{self.name} ({self.iso_code})"

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states", verbose_name="País")
    name = models.CharField(max_length=100, verbose_name="Nombre del Estado/Provincia")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        unique_together = ('country', 'name')
        ordering = ['country__name', 'name']

    @property
    def state_label(self):
        return f"{self.name} ({self.country.iso_code})"


    def __str__(self):
        return f"{self.name} ({self.country.iso_code})"

class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre de la Moneda")
    single_name = models.CharField(max_length=25, null=True, blank=True, verbose_name="Nombre en Singular")
    plural_name = models.CharField(max_length=25, null=True, blank=True, verbose_name="Nombre en Plural")
    code = models.CharField(max_length=10, unique=True, help_text="Código de 3 letras (ej. USD, VES, EUR)", verbose_name="Código de Moneda")
    symbol = models.CharField(max_length=10, verbose_name="Símbolo", help_text="Ej. $, Bs, €")
    is_active = models.BooleanField(default=True, verbose_name="¿Está activa?")

    class Meta:
        verbose_name = "Moneda"
        verbose_name_plural = "Monedas"
        ordering = ['name']

    @property
    def currency_label(self):
        return f"{self.name} ({self.code})"


    def __str__(self):
        return f"{self.name} ({self.code})"


class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base_rates", verbose_name="Moneda Base")
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="target_rates", verbose_name="Moneda Destino")
    rate = models.DecimalField(max_digits=18, decimal_places=8, verbose_name="Tasa de Cambio")
    date = models.DateField(verbose_name="Fecha de la Tasa")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tasa de Cambio"
        verbose_name_plural = "Tasas de Cambio"
        unique_together = ('base_currency', 'target_currency', 'date') # Solo una tasa por par de monedas en un día específico
        ordering = ['-date'] 

    @property
    def rate_label(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.date})"

    def __str__(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.date})"
    
