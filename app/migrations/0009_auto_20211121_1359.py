# Generated by Django 3.1.2 on 2021-11-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_informacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='url_maps',
            field=models.CharField(max_length=600),
        ),
    ]