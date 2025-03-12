from rest_framework import generics
from .models import TradingSignal, SignalType, SignalSource, Market
from .serializers import TradingSignalSerializer, SignalTypeSerializer, SignalSourceSerializer, MarketSerializer
from rest_framework import permissions

class TradingSignalList(generics.ListCreateAPIView):
    queryset = TradingSignal.objects.all()
    serializer_class = TradingSignalSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class TradingSignalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingSignal.objects.all()
    serializer_class = TradingSignalSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignalTypeList(generics.ListCreateAPIView):
    queryset = SignalType.objects.all()
    serializer_class = SignalTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignalTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SignalType.objects.all()
    serializer_class = SignalTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignalSourceList(generics.ListCreateAPIView):
    queryset = SignalSource.objects.all()
    serializer_class = SignalSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignalSourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SignalSource.objects.all()
    serializer_class = SignalSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarketList(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]
