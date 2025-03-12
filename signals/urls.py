from django.urls import path
from . import views

urlpatterns = [
    path('signals/', views.TradingSignalList.as_view(), name='signal-list'),
    path('signals/<int:pk>/', views.TradingSignalDetail.as_view(), name='signal-detail'),
    path('signaltypes/', views.SignalTypeList.as_view(), name='signaltype-list'),
    path('signaltypes/<int:pk>/', views.SignalTypeDetail.as_view(), name='signaltype-detail'),
    path('signalsources/', views.SignalSourceList.as_view(), name='signalsource-list'),
    path('signalsources/<int:pk>/', views.SignalSourceDetail.as_view(), name='signalsource-detail'),
    path('markets/', views.MarketList.as_view(), name='market-list'),
    path('markets/<int:pk>/', views.MarketDetail.as_view(), name='market-detail'),
]
