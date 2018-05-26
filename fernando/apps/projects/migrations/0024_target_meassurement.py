# Generated by Django 2.0.5 on 2018-05-26 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_planification_meassurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target_Meassurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ud_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='unidades')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('wide', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('total_meassurement', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('phase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Phase', verbose_name='phase')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Task', verbose_name='task')),
            ],
            options={
                'verbose_name': 'Target Meassurement',
                'verbose_name_plural': 'Target Meassurements',
            },
        ),
    ]
