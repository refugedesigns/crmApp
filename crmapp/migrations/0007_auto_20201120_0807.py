# Generated by Django 3.1.2 on 2020-11-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0006_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user-icon.jpg', null=True, upload_to=''),
        ),
    ]