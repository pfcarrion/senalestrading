from rest_framework import serializers
from .models import Market, SignalType, SignalSource, TradingSignal

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class SignalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalType
        fields = '__all__'

class SignalSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignalSource
        fields = '__all__'

class TradingSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingSignal
        fields = '__all__'
        depth = 1 # Incluir detalles de las relaciones (signal_type, source)
