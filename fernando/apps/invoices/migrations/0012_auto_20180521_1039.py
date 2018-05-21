# Generated by Django 2.0.5 on 2018-05-21 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180520_0450'),
        ('invoices', '0011_auto_20180521_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buying_entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.AddField(
            model_name='docket',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Project'),
        ),
    ]