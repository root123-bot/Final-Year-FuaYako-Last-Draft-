# Generated by Django 3.0 on 2021-08-12 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0083_auto_20210812_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 12, 11, 6, 4, 741697), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 14, 11, 6, 4, 740705), null=True),
        ),
    ]