# Generated by Django 3.0 on 2021-06-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210615_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]