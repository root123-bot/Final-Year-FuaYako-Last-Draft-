# Generated by Django 3.0 on 2021-08-12 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0079_auto_20210812_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 12, 10, 27, 26, 722916), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 14, 10, 27, 26, 722019), null=True),
        ),
    ]
