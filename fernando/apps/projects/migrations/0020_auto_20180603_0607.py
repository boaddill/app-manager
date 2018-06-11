# Generated by Django 2.0.5 on 2018-06-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20180531_1853'),
        ('projects', '0019_auto_20180603_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indirect_Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, max_length=200, null=True, verbose_name='Date')),
                ('valid_until', models.DateField(blank=True, null=True, verbose_name='Valid untill')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Indirect_Cost_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('units', models.CharField(blank=True, max_length=200, null=True, verbose_name='Units')),
                ('entry_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Entry name ')),
                ('description', models.TextField(blank=True, default='coments', max_length=400, null=True, verbose_name='Coments')),
                ('scope_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('scope_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('scope_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost', verbose_name='Chapter - Project')),
                ('items', models.ManyToManyField(blank=True, to='invoices.Item', verbose_name='Items')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project')),
            ],
        ),
        migrations.AddField(
            model_name='planification_meassurement',
            name='Indirect_Cost_Entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost_Entry', verbose_name='Entry'),
        ),
        migrations.AddField(
            model_name='real_meassurement',
            name='Indirect_Cost_Entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost_Entry', verbose_name='Entry'),
        ),
        migrations.AddField(
            model_name='scope_meassurement',
            name='Indirect_Cost_Entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost_Entry', verbose_name='Entry'),
        ),
        migrations.AddField(
            model_name='target_meassurement',
            name='Indirect_Cost_Entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost_Entry', verbose_name='Entry'),
        ),
    ]
