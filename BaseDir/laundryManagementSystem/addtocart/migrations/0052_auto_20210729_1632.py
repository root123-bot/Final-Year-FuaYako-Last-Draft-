# Generated by Django 3.0 on 2021-07-29 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0051_auto_20210723_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clicked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 16, 32, 40, 967400), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 31, 16, 32, 40, 966596), null=True),
        ),
    ]
