# Generated by Django 3.1.2 on 2020-11-10 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0003_order_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]