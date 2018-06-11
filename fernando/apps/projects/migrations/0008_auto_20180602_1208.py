# Generated by Django 2.0.5 on 2018-06-02 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20180602_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_name',
            field=models.CharField(max_length=200, verbose_name='Chapter name '),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Scope', verbose_name='Scope'),
        ),
    ]
