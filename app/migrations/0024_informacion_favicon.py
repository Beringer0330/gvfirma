# Generated by Django 3.1.2 on 2022-02-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_asociados_nombre_corto'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacion',
            name='favicon',
            field=models.ImageField(null=True, upload_to='Favicon'),
        ),
    ]
