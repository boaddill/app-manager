# Generated by Django 2.0.5 on 2018-05-25 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20180525_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.Tasks', verbose_name='Task'),
        ),
    ]
