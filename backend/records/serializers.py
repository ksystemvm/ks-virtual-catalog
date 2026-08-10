from rest_framework import serializers
from .models import Country, State, Currency, ExchangeRate

class CountrySerializer(serializers.ModelSerializer):
    country_label = serializers.CharField(read_only=True)
    states = serializers.SerializerMethodField()

    def get_states(self, obj):
        states = State.objects.filter(country=obj)
        return StateSerializer(states, many=True).data
    
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'iso_code',
            'phone_code',
            'is_active',
            'country_label',
            'states',
        ]

class StateSerializer(serializers.ModelSerializer):
    state_label = serializers.CharField(read_only=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = State
        fields = [
            'id',
            'country',
            'country_name',
            'name',
            'is_active',
            'state_label',
        ]

class CurrencySerializer(serializers.ModelSerializer):
    currency_label = serializers.CharField(read_only=True)

    class Meta:
        model = Currency
        fields = [
            'id',
            'name',
            'single_name',
            'plural_name',
            'code',
            'symbol',
            'is_active',
            'currency_label',
        ]

class ExchangeRateSerializer(serializers.ModelSerializer):
    base_currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())
    base_currency_code = serializers.CharField(source='base_currency.code', read_only=True)
    target_currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())
    target_currency_code = serializers.CharField(source='target_currency.code', read_only=True)

    class Meta:
        model = ExchangeRate
        fields = [
            'id',
            'base_currency',
            'base_currency_code',
            'target_currency',
            'target_currency_code',
            'rate',
            'date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id', 
            'created_at', 
            'updated_at', 
            'base_currency_code', 
            'target_currency_code'
        ]