# Generated by Django 2.0.5 on 2018-05-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180520_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_employee',
            name='hour_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile_employee',
            name='hour_price_int',
            field=models.FloatField(blank=True, null=True),
        ),
    ]