# Generated by Django 2.0.5 on 2018-05-31 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('chapter_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Chapter name ')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity_invoice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity_planif', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity_target', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity_real', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_invoice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_planif', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_target', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_real', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Actual chapter price')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Entry name ')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('description', models.TextField(blank=True, default='coments', max_length=400, null=True, verbose_name='Coments')),
                ('scope_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('invoice_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('scope_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('invoice_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_unt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('scope_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('invoice_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'verbose_name': 'Project Entry',
                'verbose_name_plural': 'Project Entries',
            },
        ),
        migrations.CreateModel(
            name='Entry_Item_Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_per_entry_unit_scope', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='quantity per entry scope')),
                ('quantity_per_entry_unit_real', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='quanatity per entry real')),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('price_per_entry_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('price_per_entry_unit_real', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Actual Price per Entry unit')),
                ('quantity_needed', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Estimated quantity needed')),
                ('quantity_bought', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='quantity_bought')),
            ],
            options={
                'verbose_name': 'Project Price',
                'verbose_name_plural': 'Project Prices',
            },
        ),
        migrations.CreateModel(
            name='Invoice_Meassurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.CharField(blank=True, max_length=200, null=True, verbose_name='coments')),
                ('ud_type', models.CharField(blank=True, max_length=9, null=True, verbose_name='unidades')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('wide', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_meassurement', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'verbose_name': 'Invoice Meassurement',
                'verbose_name_plural': 'invoice Meassurements',
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_code', models.IntegerField()),
                ('phase_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phase name ')),
                ('coments', models.TextField(blank=True, default='coments', max_length=400, null=True, verbose_name='coments')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('scope_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('invoice_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('planif_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('target_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('real_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Actual price')),
            ],
        ),
        migrations.CreateModel(
            name='Planification_Meassurement',
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
                'verbose_name': 'Planification Meassurement',
                'verbose_name_plural': 'Planification Meassurements',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=200, null=True)),
                ('project_number', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('project_address', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('state', models.CharField(choices=[('ACT', 'Accepted'), ('WFA', 'Waiting'), ('REJ', 'Overruled')], default='WFA', max_length=3)),
            ],
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
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Entry', verbose_name='entry')),
                ('phase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Phase', verbose_name='phase')),
            ],
            options={
                'verbose_name': 'Real Meassurement',
                'verbose_name_plural': 'Real Meassurements',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('date', models.DateField(blank=True, max_length=200, null=True, verbose_name='Date')),
                ('valid_until', models.DateField(blank=True, null=True, verbose_name='Valid untill')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_invoice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_planif', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_target', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price_real', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Construction actual Price')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Scope_Meassurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.CharField(blank=True, max_length=200, null=True, verbose_name='coments')),
                ('ud_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='unidades')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('wide', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_meassurement', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Entry', verbose_name='Entry')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Phase', verbose_name='phase')),
            ],
            options={
                'verbose_name': 'Scope Meassurement',
                'verbose_name_plural': 'Scope Meassurements',
            },
        ),
        migrations.CreateModel(
            name='Target_Meassurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments', models.CharField(blank=True, max_length=200, null=True, verbose_name='coments')),
                ('ud_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='unidades')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('wide', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_meassurement', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Entry', verbose_name='entry')),
                ('phase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Phase', verbose_name='phase')),
            ],
            options={
                'verbose_name': 'Target Meassurement',
                'verbose_name_plural': 'Target Meassurements',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Code')),
                ('task_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Task name ')),
                ('description', models.TextField(blank=True, default='coments', max_length=400, null=True, verbose_name='coments')),
            ],
        ),
    ]
