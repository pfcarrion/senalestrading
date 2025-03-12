# Generated by Django 5.1.6 on 2025-02-27 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignalSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_automated', models.BooleanField(default=False)),
                ('source_type', models.CharField(blank=True, max_length=50, null=True)),
                ('config', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SignalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_frame', models.CharField(blank=True, max_length=50, null=True)),
                ('min_subscription_level', models.IntegerField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.market')),
            ],
        ),
        migrations.CreateModel(
            name='TradingSignal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=10)),
                ('entry_price', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('take_profit', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('stop_loss', models.DecimalField(blank=True, decimal_places=8, max_digits=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('signal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.signaltype')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signals.signalsource')),
            ],
        ),
    ]
