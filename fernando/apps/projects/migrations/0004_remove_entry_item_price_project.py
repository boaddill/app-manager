# Generated by Django 2.0.5 on 2018-05-31 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_entry_item_price_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry_item_price',
            name='project',
        ),
    ]