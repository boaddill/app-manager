# Generated by Django 2.0.5 on 2018-06-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_entry_item_price_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='entry',
            name='benefit_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='custom_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
    ]