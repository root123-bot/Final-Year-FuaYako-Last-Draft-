# Generated by Django 3.0 on 2021-08-04 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_companyprofile_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='photo',
            field=models.ImageField(default='images/profile.png', upload_to='images/'),
        ),
    ]
