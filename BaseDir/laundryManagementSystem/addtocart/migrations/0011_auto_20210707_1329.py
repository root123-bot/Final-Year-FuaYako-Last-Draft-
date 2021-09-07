# Generated by Django 3.0 on 2021-07-07 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0010_auto_20210707_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 7, 13, 29, 58, 864639), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 9, 13, 29, 58, 863826), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderID',
            field=models.CharField(default='08S9C4M9OCQ3NJ2UDER4ZBULG', max_length=25),
        ),
    ]
