# Generated by Django 2.0.5 on 2018-06-09 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20180609_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry_item_price',
            name='price_per_entry_unit',
        ),
    ]
