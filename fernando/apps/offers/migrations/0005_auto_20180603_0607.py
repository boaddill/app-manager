# Generated by Django 2.0.5 on 2018-06-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_auto_20180602_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitude_entry',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Entry_Item_Price', verbose_name='Item'),
        ),
    ]
