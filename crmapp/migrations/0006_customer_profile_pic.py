# Generated by Django 3.1.2 on 2020-11-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0005_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
