# Generated by Django 4.0 on 2022-03-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0004_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
