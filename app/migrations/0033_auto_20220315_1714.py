# Generated by Django 3.1.2 on 2022-03-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20220312_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing',
            name='correo',
            field=models.CharField(max_length=600),
        ),
    ]
