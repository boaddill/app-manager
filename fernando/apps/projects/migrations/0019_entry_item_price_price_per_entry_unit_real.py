# Generated by Django 2.0.5 on 2018-05-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20180529_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_item_price',
            name='price_per_entry_unit_real',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]