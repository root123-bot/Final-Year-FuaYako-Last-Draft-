# Generated by Django 3.0 on 2021-07-06 10:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0006_auto_20210705_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 6, 10, 5, 42, 677380), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 8, 10, 5, 42, 676566), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='mode',
            field=models.CharField(blank=True, choices=[('Pick at station', 'Pick at station'), ('Door step pickup', 'Door step pickup')], default='Pick at station', max_length=100, null=True),
        ),
    ]