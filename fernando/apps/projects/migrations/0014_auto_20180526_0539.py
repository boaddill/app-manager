# Generated by Django 2.0.5 on 2018-05-26 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_remove_task_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope_meassurements',
            name='phase',
        ),
        migrations.RemoveField(
            model_name='scope_meassurements',
            name='task',
        ),
        migrations.DeleteModel(
            name='Scope_Meassurements',
        ),
    ]
