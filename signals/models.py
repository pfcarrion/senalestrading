from django.db import models
from django.db.models import JSONField  # Importante: usa django.db.models.JSONField

class Market(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SignalType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    time_frame = models.CharField(max_length=50, blank=True, null=True)
    min_subscription_level = models.IntegerField()

    def __str__(self):
        return self.name

class SignalSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_automated = models.BooleanField(default=False)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    config = models.JSONField(default=dict)  # Importante: usa models.JSONField

    def __str__(self):
        return self.name

class TradingSignal(models.Model):
    signal_type = models.ForeignKey(SignalType, on_delete=models.CASCADE)
    source = models.ForeignKey(SignalSource, on_delete=models.CASCADE)
    asset = models.CharField(max_length=100)
    direction = models.CharField(max_length=10)
    entry_price = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    take_profit = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    stop_loss = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, default='active')

    def __str__(self):
        return f"{self.asset} - {self.direction} - {self.signal_type.name}"
