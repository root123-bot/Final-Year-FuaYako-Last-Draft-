# Generated by Django 3.0 on 2021-08-05 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0071_auto_20210804_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 5, 1, 15, 15, 688744), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 7, 1, 15, 15, 687692), null=True),
        ),
    ]