# Generated by Django 2.0.5 on 2018-06-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20180603_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='real_meassurement',
            name='Indirect_Cost_Entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Indirect_Cost_Entry', verbose_name='Indirect cost'),
        ),
    ]
