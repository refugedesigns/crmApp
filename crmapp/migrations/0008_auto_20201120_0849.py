# Generated by Django 3.1.2 on 2020-11-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0007_auto_20201120_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user-icon.jpg', null=True, upload_to='img'),
        ),
    ]
