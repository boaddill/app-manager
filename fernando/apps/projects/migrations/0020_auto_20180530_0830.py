# Generated by Django 2.0.5 on 2018-05-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_entry_item_price_price_per_entry_unit_real'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='total_price_invoice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='total_price_planif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='total_price_real',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='total_price_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='entry_item_price',
            name='quantity_per_entry_unit_real',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='quanatity per entry real'),
        ),
        migrations.AlterField(
            model_name='entry_item_price',
            name='quantity_per_entry_unit_scope',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='quantity per entry scope'),
        ),
    ]
