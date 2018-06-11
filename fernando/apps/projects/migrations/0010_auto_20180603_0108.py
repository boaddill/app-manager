# Generated by Django 2.0.5 on 2018-06-03 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_entry_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry_item_price',
            name='item_price_scope',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry_item_price',
            name='scope',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Scope', verbose_name='Scope'),
        ),
        migrations.AddField(
            model_name='scope',
            name='benefit_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='custom_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='general_cost_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='scope',
            name='indirect_cost_factor',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='planification_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='real_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='scope_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='units'),
        ),
        migrations.AlterField(
            model_name='target_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='units'),
        ),
    ]
