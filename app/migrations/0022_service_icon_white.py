# Generated by Django 3.1.2 on 2022-02-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20211124_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon_white',
            field=models.ImageField(null=True, upload_to='services_icon'),
        ),
    ]
