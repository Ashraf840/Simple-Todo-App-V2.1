# Generated by Django 3.2.3 on 2021-06-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_auto_20210606_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mytodo',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='mytodo',
            name='last_login',
        ),
        migrations.AddField(
            model_name='mytodo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='mytodo',
            name='last_updated_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified on'),
        ),
    ]