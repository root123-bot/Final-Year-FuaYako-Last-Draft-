# Generated by Django 3.0 on 2021-08-04 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0004_auto_20210804_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='account_number',
            field=models.CharField(max_length=25),
        ),
    ]