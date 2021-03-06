# Generated by Django 3.0 on 2021-08-02 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0057_auto_20210801_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='assigned_To',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 2, 7, 47, 53, 51500), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 4, 7, 47, 53, 50692), null=True),
        ),
    ]
