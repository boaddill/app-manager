# Generated by Django 2.0.5 on 2018-05-28 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180528_0957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='scope_unit_price',
            new_name='scope_unt_price',
        ),
    ]