# Generated by Django 2.0.5 on 2018-06-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0036_auto_20180614_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope_meassurement',
            name='coments',
            field=models.CharField(blank=True, help_text='coments', max_length=200, null=True, verbose_name='coments'),
        ),
        migrations.AlterField(
            model_name='scope_meassurement',
            name='ud_type',
            field=models.CharField(blank=True, help_text='units', max_length=200, null=True, verbose_name='units'),
        ),
    ]