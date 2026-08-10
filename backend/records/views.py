from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from .models import Country, State, Currency, ExchangeRate
from .serializers import CountrySerializer, StateSerializer, CurrencySerializer, ExchangeRateSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.filter(is_active=True)
    serializer_class = StateSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.filter(is_active=True)
    serializer_class = CurrencySerializer

class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    @action(detail=False, methods=['post'], url_path='bulk-create')
    def bulk_create_rates(self, request):
        
        target_currency_id = request.data.get('target_currency')
        effective_date = request.data.get('effective_date')
        rates = request.data.get('rates', [])

        if not target_currency_id or not effective_date or not rates:
            return Response({"detail": "Faltan datos obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

        created_count = 0
        updated_count = 0

        try:
            with transaction.atomic():
                for item in rates:
                    rate = item.get('rate_value')
                    base_currency_id = item.get('source_currency_id')
                    if rate:
                        obj, created = ExchangeRate.objects.update_or_create(
                            target_currency_id=target_currency_id,
                            base_currency_id=base_currency_id,
                            date=effective_date,
                            defaults={'rate': rate}
                        )
                        if created:
                            created_count += 1
                        else:
                            updated_count += 1
            return Response({
                "detail": f"¡Éxito! {created_count} tasas nuevas creadas y {updated_count} actualizadas."
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"detail": f"Error al procesar: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = ExchangeRate.objects.all()
        target = self.request.query_params.get('target_currency')
        fecha = self.request.query_params.get('date')
        
        if target:
            queryset = queryset.filter(target_currency_id=target)
        if fecha:
            queryset = queryset.filter(date=fecha)
        return queryset