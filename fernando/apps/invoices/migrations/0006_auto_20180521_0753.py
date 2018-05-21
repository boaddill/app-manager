# Generated by Django 2.0.5 on 2018-05-21 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180520_1151'),
        ('projects', '0002_auto_20180520_0450'),
        ('invoices', '0005_auto_20180520_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buying_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('units', models.CharField(blank=True, max_length=200, null=True, verbose_name='units')),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('invoiced', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Docket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('date', models.DateField(verbose_name='date')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile_Client', verbose_name='Client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='item',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='project',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='task',
        ),
        migrations.AddField(
            model_name='item',
            name='code',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.FloatField(default=None, verbose_name='Item price'),
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='docket',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='docket', to='invoices.Docket', verbose_name='Docket'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='invoice',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='invoices.Invoice', verbose_name='Invoice'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Item', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='invoices.Order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile_Provider', verbose_name='Provider'),
        ),
        migrations.AddField(
            model_name='buying_entry',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.Tasks', verbose_name='Task'),
        ),
    ]