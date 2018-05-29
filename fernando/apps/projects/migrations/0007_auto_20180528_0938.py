# Generated by Django 2.0.5 on 2018-05-28 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20180527_1250'),
        ('projects', '0006_auto_20180527_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_Item_Price_Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'verbose_name': 'Project Price',
                'verbose_name_plural': 'Project Prices',
            },
        ),
        migrations.CreateModel(
            name='Real_Meassurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.CharField(blank=True, max_length=200, null=True, verbose_name='coments')),
                ('ud_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='unidades')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('wide', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_meassurement', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'verbose_name': 'Real Meassurement',
                'verbose_name_plural': 'Real Meassurements',
            },
        ),
        migrations.RemoveField(
            model_name='project_price',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='project_price',
            name='project',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='unit_price',
            new_name='planif_quantity',
        ),
        migrations.AddField(
            model_name='entry',
            name='real_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='real_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='real_unt_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='scope_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='traget_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.DeleteModel(
            name='Project_Price',
        ),
        migrations.AddField(
            model_name='real_meassurement',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Entry', verbose_name='entry'),
        ),
        migrations.AddField(
            model_name='real_meassurement',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Phase', verbose_name='phase'),
        ),
        migrations.AddField(
            model_name='entry_item_price_target',
            name='entry',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Entry', verbose_name='Entry'),
        ),
        migrations.AddField(
            model_name='entry_item_price_target',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.Item', verbose_name='Entry'),
        ),
        migrations.AddField(
            model_name='entry_item_price_target',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project'),
        ),
    ]
