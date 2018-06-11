# Generated by Django 2.0.5 on 2018-06-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0033_auto_20180610_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_item_price',
            name='item_price_invoice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Item Price [invoice]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='item_price_planif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Item Price [planif]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='item_price_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Item Price [target]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='price_per_entry_unit_invoice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price/Entry Unit [Invoice]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='price_per_entry_unit_planif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price/Entry Unit [planif]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='price_per_entry_unit_target',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price/Entry Unit [Target]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='quantity_per_entry_unit_invoice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Quantity/Entry [Invoiced]'),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='quantity_per_entry_unit_planif',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Quantity/Entry [Panif]'),
        ),
        migrations.AlterField(
            model_name='entry_item_price',
            name='quantity_per_entry_unit_scope',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Quantity/Entry [Target]'),
        ),
    ]
