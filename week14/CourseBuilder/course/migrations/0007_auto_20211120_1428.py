# Generated by Django 3.2.7 on 2021-11-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20211119_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='document',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='html',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='markdown',
        ),
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='week',
            field=models.IntegerField(null=True),
        ),
    ]
