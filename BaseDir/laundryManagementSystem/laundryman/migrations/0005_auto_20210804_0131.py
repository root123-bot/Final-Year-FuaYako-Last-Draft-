# Generated by Django 3.0 on 2021-08-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundryman', '0004_laundryprofile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundryprofile',
            name='photo',
            field=models.ImageField(default='images/profile.png', upload_to='images/'),
        ),
    ]
