# Generated by Django 3.1.2 on 2020-11-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_category_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]