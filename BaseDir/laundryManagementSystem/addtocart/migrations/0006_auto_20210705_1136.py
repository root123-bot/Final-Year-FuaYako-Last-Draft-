# Generated by Django 3.0 on 2021-07-05 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtocart', '0005_auto_20210705_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='arrived_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 5, 11, 36, 5, 540831), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='finished_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 7, 11, 36, 5, 539978), null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='mode',
            field=models.CharField(blank=True, choices=[('Pick at station', 'Pick at station'), ('Door step pickup', 'Door step pickup')], max_length=100, null=True),
        ),
    ]
