# Generated by Django 2.0.5 on 2018-06-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180601_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_item_price',
            name='price_per_entry_unit_scope',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
