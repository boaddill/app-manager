# Generated by Django 2.0.5 on 2018-05-29 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20180527_1250'),
        ('projects', '0013_auto_20180529_0904'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry_Item_Price_Target',
            new_name='Entry_Item_Price',
        ),
    ]
